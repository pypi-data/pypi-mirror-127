import logging
import typing as tp

import substrateinterface as substrate

from scalecodec.types import GenericCall, GenericExtrinsic

from .constants import REMOTE_WS, TYPE_REGISTRY
from .exceptions import NoPrivateKey

Datalog = tp.Dict[str, tp.Union[int, str]]
NodeTypes = tp.Dict[str, tp.Dict[str, tp.Union[str, tp.Any]]]


class RobonomicsInterface:
    """
    A class for establishing connection to the Robonomics nodes and interacting with them.
    Fetch chainstate, submit extrinsics, custom calls.
    """

    def __init__(
        self,
        seed: tp.Optional[str] = None,
        remote_ws: tp.Optional[str] = None,
        type_registry: tp.Optional[NodeTypes] = None,
    ) -> None:
        """
        Instance of a class is an interface with a node. Here this interface is initialized.

        @param seed: account seed in mnemonic/raw form. When not passed, no extrinsics functionality
        @param remote_ws: node url. Default node address is "wss://main.frontier.rpc.robonomics.network".
        Another address may be specified (e.g. "ws://127.0.0.1:9944" for local node).
        @param type_registry: types used in the chain. Defaults are the most frequently used in Robonomics
        """

        self.interface: substrate.SubstrateInterface
        self._keypair: tp.Optional[substrate.Keypair] = self._create_keypair(seed) if seed else None

        if not self._keypair:
            logging.warning("No seed specified, you won't be able to sign extrinsics, fetching chainstate only.")

        if type_registry:
            logging.warning("Using custom type registry for the node")

        logging.info("Establishing connection with Robonomics node")
        self.interface = self._establish_connection(remote_ws or REMOTE_WS, type_registry or TYPE_REGISTRY)

        logging.info("Successfully established connection to Robonomics node")

    @staticmethod
    def _create_keypair(seed: str) -> substrate.Keypair:
        """
        Create a keypair for further use

        @param seed: user seed as a key to sign transactions

        @return: a Keypair instance used by substrate to sign transactions
        """

        if seed.startswith("0x"):
            return substrate.Keypair.create_from_seed(seed_hex=hex(int(seed, 16)), ss58_format=32)
        else:
            return substrate.Keypair.create_from_mnemonic(seed, ss58_format=32)

    @staticmethod
    def _establish_connection(url: str, types: NodeTypes) -> substrate.SubstrateInterface:
        """
        Create a substrate interface for interacting wit Robonomics node

        @param url: node endpoint
        @param types: json types used by pallets

        @return: interface of a Robonomics node connection
        """

        return substrate.SubstrateInterface(
            url=url,
            ss58_format=32,
            type_registry_preset="substrate-node-template",
            type_registry=types,
        )

    def custom_chainstate(
        self,
        module: str,
        storage_function: str,
        params: tp.Optional[tp.Union[tp.List[tp.Union[str, int]], str, int]] = None,
    ) -> tp.Any:
        """
        Create custom queries to fetch data from the Chainstate. Module names and storage functions, as well as required
        parameters are available at https://parachain.robonomics.network/#/chainstate

        @param module: chainstate module
        @param storage_function: storage function
        @param params: query parameters. None if no parameters. Include in list, if several

        @return: output of the query in any form
        """

        logging.info("Performing query")
        return self.interface.query(module, storage_function, [params] if params else None)

    def _define_address(self) -> str:
        """
        define ss58_address of an account, which seed was provided while initializing an interface

        @return: ss58_address of an account
        """

        if not self._keypair:
            raise NoPrivateKey("No private key was provided, unable to determine self address")
        return str(self._keypair.ss58_address)

    def fetch_datalog(self, addr: tp.Optional[str] = None, index: tp.Optional[int] = None) -> tp.Optional[Datalog]:
        """
        Fetch datalog record of a provided account. Fetch self datalog if no address provided and interface was
        initialized with a seed.

        @param addr: ss58 type 32 address of an account which datalog is to be fetched. If None, tries to fetch self
        datalog if keypair was created, else raises NoPrivateKey
        @param index: record index. case int: fetch datalog by specified index
                                    case None: fetch latest datalog

        @return: Dictionary. Datalog of the account with a timestamp, None if no records.
        """

        _address: str = addr or self._define_address()

        logging.info(
            f"Fetching {'latest datalog record' if not index else 'datalog record #' + str(index)}" f" of {_address}."
        )

        if index:
            _record: Datalog = self.custom_chainstate("Datalog", "DatalogItem", [_address, index]).value
            return _record if _record["timestamp"] != 0 else None
        else:
            _index_latest: int = self.custom_chainstate("Datalog", "DatalogIndex", _address).value["end"] - 1
            return (
                self.custom_chainstate("Datalog", "DatalogItem", [_address, _index_latest]).value
                if _index_latest != -1
                else None
            )

    def custom_extrinsic(
        self,
        call_module: str,
        call_function: str,
        params: tp.Optional[tp.Dict[str, tp.Any]] = None,
        nonce: tp.Optional[int] = None,
    ) -> str:
        """
        Create an extrinsic, sign&submit it. Module names and functions, as well as required parameters are available
        at https://parachain.robonomics.network/#/extrinsics

        @param call_module: Call module from extrinsic tab
        @param call_function: Call function from extrinsic tab
        @param params: Call parameters as a dictionary. None for no parameters
        @param nonce: transaction nonce, defined automatically if None. Due to e feature of substrate-interface lib,
        to create an extrinsic with incremented nonce, pass account's current nonce. See
        https://github.com/polkascan/py-substrate-interface/blob/85a52b1c8f22e81277907f82d807210747c6c583/substrateinterface/base.py#L1535
        for example.

        @return: Extrinsic hash or None if failed
        """

        if not self._keypair:
            raise NoPrivateKey("No seed was provided, unable to use extrinsics.")

        logging.info(f"Creating a call {call_module}:{call_function}")
        _call: GenericCall = self.interface.compose_call(
            call_module=call_module,
            call_function=call_function,
            call_params=params or None,
        )

        logging.info("Creating extrinsic")
        _extrinsic: GenericExtrinsic = self.interface.create_signed_extrinsic(
            call=_call, keypair=self._keypair, nonce=nonce
        )

        logging.info("Submitting extrinsic")
        _receipt: substrate.ExtrinsicReceipt = self.interface.submit_extrinsic(_extrinsic, wait_for_inclusion=True)
        logging.info(
            f"Extrinsic {_receipt.extrinsic_hash} for RPC {call_module}:{call_function} submitted and "
            f"included in block {_receipt.block_hash}"
        )

        return str(_receipt.extrinsic_hash)

    def record_datalog(self, data: str, nonce: tp.Optional[int] = None) -> str:
        """
        Write any string to datalog

        @param data: string to be stored in datalog
        @param nonce: nonce of the transaction. Due to e feature of substrate-interface lib,
        to create an extrinsic with incremented nonce, pass account's current nonce. See
        https://github.com/polkascan/py-substrate-interface/blob/85a52b1c8f22e81277907f82d807210747c6c583/substrateinterface/base.py#L1535
        for example.

        @return: Hash of the datalog transaction
        """

        logging.info(f"Writing datalog {data}")
        return self.custom_extrinsic("Datalog", "record", {"record": data}, nonce)

    def send_launch(self, target_address: str, toggle: bool, nonce: tp.Optional[int] = None) -> str:
        """
        Send Launch command to device

        @param target_address: device to be triggered with launch
        @param toggle: whether send ON or OFF command. ON == True, OFF == False
        @param nonce: account nonce. Due to e feature of substrate-interface lib,
        to create an extrinsic with incremented nonce, pass account's current nonce. See
        https://github.com/polkascan/py-substrate-interface/blob/85a52b1c8f22e81277907f82d807210747c6c583/substrateinterface/base.py#L1535
        for example.

        @return: Hash of the launch transaction
        """

        logging.info(f"Sending {'ON' if toggle else 'OFF'} launch command to {target_address}")
        return self.custom_extrinsic("Launch", "launch", {"robot": target_address, "param": toggle}, nonce)

    def get_account_nonce(self, account_address: tp.Optional[str] = None) -> int:
        """
        Get current account nonce

        @param account_address: account ss58_address. Self address via private key is obtained if not passed.

        @return account nonce. Due to e feature of substrate-interface lib,
        to create an extrinsic with incremented nonce, pass account's current nonce. See
        https://github.com/polkascan/py-substrate-interface/blob/85a52b1c8f22e81277907f82d807210747c6c583/substrateinterface/base.py#L1535
        for example.
        """

        return self.interface.get_account_nonce(account_address=account_address or self._define_address())

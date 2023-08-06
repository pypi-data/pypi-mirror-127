from lunespy.utils import export_json
from lunespy.utils import log_data
from lunespy.utils import bcolors
from lunespy.server import Node
from abc import abstractmethod
from abc import ABCMeta


class BaseTransaction(metaclass=ABCMeta):
    def __init__(self, tx_type: str, tx_data: dict):
        self.tx_type: str = tx_type
        self.tx_data: str = tx_data

    @abstractmethod
    def ready(self) -> bool:
        raise NotImplementedError


    def transaction(self, mount_tx, **extra) -> dict:
        if self.ready:
            tx = {'ready': True}
            tx.update( mount_tx( **extra ) )
            return tx
        else:
            print(bcolors.FAIL + f'{self.tx_type} Transactions bad formed', bcolors.ENDC)
            return {'ready': False}


    def send(self, send_tx, node_url: str) -> dict:
        if node_url == None:
            if self.sender.network == 'mainnet':
                node_url = Node.mainnet_url.value
            else:
                node_url = Node.testnet_url.value

        mounted_tx = self.transaction
        if mounted_tx['ready']:
            tx_response = send_tx(mounted_tx, node_url=node_url)

            if tx_response['send']:
                self.show(**tx_response)
                return tx_response
            else:
                print(bcolors.FAIL + f"Your {self.tx_type} dont sended because:\n└──{tx_response['response']}" + bcolors.ENDC)
                return tx_response

        else:
            print(bcolors.FAIL + f'{self.tx_type} Transaction dont send', bcolors.ENDC)
            return mounted_tx
        

    def show(self, **data: dict) -> None:
        log_data(data)
        export_json(data)

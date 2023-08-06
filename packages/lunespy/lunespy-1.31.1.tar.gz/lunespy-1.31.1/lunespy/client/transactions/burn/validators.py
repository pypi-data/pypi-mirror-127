from lunespy.utils.crypto.converters import bytes_to_string
from lunespy.utils.crypto.converters import string_to_bytes
from lunespy.client.transactions.constants import BurnType
from lunespy.utils.crypto.converters import sign
from lunespy.utils import bcolors
from lunespy.client.wallet import Account
from lunespy.utils import now
from base58 import b58decode
from requests import post
import struct


def mount_burn(sender: Account, burn_data: dict) -> dict:
    timestamp: int = burn_data.get('timestamp', int(now() * 1000))
    burn_fee: int = burn_data.get('burn_fee', BurnType.fee.value)
    quantity: int = burn_data.get('quantity', 0)
    asset_id: int = burn_data['asset_id']

    bytes_data: bytes = BurnType.to_byte.value + \
        b58decode(sender.public_key) + \
        b58decode(asset_id) + \
        struct.pack(">Q", quantity) + \
        struct.pack(">Q", burn_fee) + \
        struct.pack(">Q", timestamp)

    signature: bytes = sign(sender.private_key, bytes_data)
    mount_tx = {
        "type": BurnType.to_int.value,
        "senderPublicKey": sender.public_key,
        "signature": signature.decode(),
        "timestamp": timestamp,
        "fee": burn_fee,

        "assetId": asset_id,
        "quantity": quantity
    }
    return mount_tx


def validate_burn(sender: Account, burn_data: dict) -> bool:
    quantity: int = burn_data.get('quantity', -1)
    asset_id: str = burn_data.get('asset_id', False)

    if not sender.private_key:
        print(bcolors.FAIL + 'Burner `Account` not have a private key' + bcolors.ENDC)
        return False

    if quantity < 0:
        print(bcolors.FAIL + 'Burn `quantity` cannot be less than 0' + bcolors.ENDC)
        return False

    if asset_id == False:
        print(bcolors.FAIL + 'Burn_data `asset_id` cannot exists' + bcolors.ENDC)
        return False

    return True


# todo async
def send_burn(mount_tx: dict, node_url: str) -> dict:
    response = post(
        f'{node_url}/transactions/broadcast',
        json=mount_tx,
        headers={
            'content-type':
            'application/json'
        })

    if response.ok:
        mount_tx.update({
            'send': True,
            'response': response.json()
        })
        return mount_tx
    else:
        mount_tx.update({
            'send': True,
            'response': response.json()
        })
        return mount_tx

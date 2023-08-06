from lunespy.client.transactions.constants import AliasType
from lunespy.utils.crypto.converters import string_to_bytes
from lunespy.utils.crypto.converters import sign
from lunespy.utils import bcolors
from lunespy.client.wallet import Account
from lunespy.utils import now
from base58 import b58decode
from requests import post
import struct

def validate_alias(sender: Account, alias_data: dict) -> bool:
    alias: int = alias_data.get('alias', False)
    valid_alias_characters =  "-.0123456789@_abcdefghijklmnopqrstuvwxyz"

    if not sender.private_key:
        print(bcolors.FAIL + 'Sender `Account` not have a private key' + bcolors.ENDC)
        return False

    if alias == False:
        print(bcolors.FAIL + 'Alias_data `alias` dont exists' + bcolors.ENDC)
        return False
    
    if not all(each_char in valid_alias_characters for each_char in alias):
        print(
            bcolors.FAIL + \
            "`Alias` should contain only following characters: -.0123456789@_abcdefghijklmnopqrstuvwxyz" + \
            bcolors.ENDC)
        return False
    
    
    return True

def mount_alias(sender: Account, alias_data: dict) -> dict:
    timestamp: int = alias_data.get('timestamp', int(now() * 1000))
    alias_fee: int = alias_data.get('alias_fee', AliasType.fee.value)
    alias: str = alias_data['alias']
    alias_lenght: int = len(alias)
    network_id: str = sender.network_id
    
    aliasWithNetwork = AliasType.mount.value +\
        string_to_bytes(str(network_id)) + \
        struct.pack(">H", len(alias)) + \
        string_to_bytes(alias)

    bytes_data = AliasType.to_byte.value + \
        b58decode(sender.public_key) + \
        struct.pack(">H", len(aliasWithNetwork)) + \
        aliasWithNetwork + \
        struct.pack(">Q", alias_fee) + \
        struct.pack(">Q", timestamp)

    signature: bytes = sign(sender.private_key, bytes_data)

    mount_tx = {
        "type": AliasType.to_int.value,
        "senderPublicKey": sender.public_key,
        "signature": signature.decode(),
        "timestamp": timestamp,
        "fee": alias_fee,

        "alias": alias
    }
    return mount_tx

def send_alias(mount_tx: dict, node_url: str) -> dict:
    
    
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
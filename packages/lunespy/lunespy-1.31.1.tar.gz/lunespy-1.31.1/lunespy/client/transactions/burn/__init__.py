from lunespy.client.transactions.burn.validators import validate_burn
from lunespy.client.transactions.burn.validators import mount_burn
from lunespy.client.transactions.burn.validators import send_burn
from lunespy.client.transactions import BaseTransaction
from lunespy.client.wallet import Account



class BurnToken(BaseTransaction):
    """
    burn_data: dict
        timestamp: int 
        asset_id: str 
        quantity: int
        burn_fee: int
    """
    def __init__(self, sender: Account, **burn_data: dict) -> None:
        super().__init__('Burn Token', burn_data)
        self.sender = sender
        self.burn_data = burn_data
        self.burn_data['token_type'] = 'Token'
        self.history = []

    @property
    def ready(self) -> bool:
        return validate_burn(self.sender, self.burn_data)
    
    @property
    def transaction(self) -> dict:
        return super().transaction(
            mount_tx=mount_burn,
            sender=self.sender,
            burn_data=self.burn_data)

    def send(self, node_url: str = None) -> dict:
        tx = super().send(send_burn, node_url)
        self.history.append(tx)
        return tx


class BurnAsset(BurnToken):
    def __init__(self, sender: Account, **burn_data: dict) -> None:
        burn_data['token_type'] = burn_data['token_type'] if burn_data.get('token_type', False) else 'Asset'
        BaseTransaction.__init__(self, tx_type='Burn Asset', tx_data=burn_data)
        BurnToken.__init__(self, sender=sender, **burn_data)


class BurnNFT(BurnAsset):
    def __init__(self,
        sender: Account,
        **burn_data: dict
        ) -> None:
        burn_data['token_type'] = 'NFT'
        BaseTransaction.__init__(self, tx_type='Burn NFT', tx_data=burn_data)
        BurnToken.__init__(self, sender=sender, **burn_data)

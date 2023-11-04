from web3 import Web3

class SendTx:
    def __init__(self,chainRpcUrl) -> None:
        self.wb3 = Web3(Web3.HTTPProvider(chainRpcUrl))
        if self.wb3.is_connected() != True:
            raise ValueError('web3 connected falied.')   
    
    def send_sign_tx(self,txdata,address_from,private_key):
        estGas = self.wb3.eth.estimate_gas(txdata)
        if estGas > self.wb3.eth.get_balance(address_from):
            print("Insufficient gas balance.")

        signTx = self.wb3.eth.account.sign_transaction(txdata, private_key)
        hash = self.wb3.eth.send_raw_transaction(signTx.rawTransaction)
        print("Transaction sent with hash:", hash.hex())
        return hash.hex()
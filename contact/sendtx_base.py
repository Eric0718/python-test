import logging
logging.basicConfig(level=logging.INFO)
import web3

class SendTx:
    def __init__(self,chainRpcUrl):
        self.wb3 = web3.Web3(web3.Web3.HTTPProvider(chainRpcUrl))
        if self.wb3.is_connected() != True:
            raise ValueError('web3 connected falied.')   
    
    def send_sign_tx(self,txdata,address_from,private_key):
        estGas = self.wb3.eth.estimate_gas(txdata)
        if estGas > self.wb3.eth.get_balance(address_from):
            logging.ERROR("estimate_gas insufficient gas balance.")
            
        signTx = self.wb3.eth.account.sign_transaction(txdata, private_key)
        hash = self.wb3.eth.send_raw_transaction(signTx.rawTransaction)
        return hash.hex()
import sendtx_base 
import json

class Petcat(sendtx_base.SendTx):
    def __init__(self,abifile,chainRpcUrl,contractAddr) -> None:
        super().__init__(chainRpcUrl)
        try:
            with open(abifile,'r') as BDBABI:
                contract_abi = json.load(BDBABI)
        except Exception as e:
            raise ValueError(f'open abi file failed:{e}')  

        self.chainRpcUrl = chainRpcUrl
        self.contractAddr = contractAddr
        self.contractobj = self.wb3.eth.contract(address=self.contractAddr, abi=contract_abi)

    def getConfig(self):
        return self.chainRpcUrl,self.contractAddr

    def new_feed_tx(self,address_from,info,amount,gas_limit): 
        tx_data =  self.contractobj.functions.feed(info,amount).build_transaction({
            'chainId': self.wb3.eth.chain_id,  
            'gas': gas_limit,
            'gasPrice': self.wb3.eth.gas_price,
            'nonce': self.wb3.eth.get_transaction_count(address_from),   
            'from':address_from, 
        })
        return tx_data

    def new_buyNft_tx(self,address_from,info,amount,gas_limit): 
        tx_data =  self.contractobj.functions.buyNFT(info,amount).build_transaction({
            'chainId': self.wb3.eth.chain_id,  
            'gas': gas_limit,
            'gasPrice': self.wb3.eth.gas_price,
            'nonce': self.wb3.eth.get_transaction_count(address_from),   
            'from':address_from, 
        })
        return tx_data



 




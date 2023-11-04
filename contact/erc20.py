import sendtx_base 
from dotenv import load_dotenv
import os

import json
import sys

load_dotenv()

class ERC20(sendtx_base.SendTx):
    def __init__(self,abifile,chainRpcUrl,tokenAddress):
        super().__init__(chainRpcUrl)
        self.chainRpcUrl = chainRpcUrl
        self.token_address = tokenAddress
        
        try:
            with open(abifile,'r') as erc20ABI:
                erc20_abi = json.load(erc20ABI) 
        except Exception as e:
            raise ValueError(f'open abi file failed:{e}')       

        self.tokenobj = self.wb3.eth.contract(address=self.token_address, abi=erc20_abi)
    
    def getConfig(self):
        return self.chainRpcUrl,self.token_address

    def symbol(self):
        return self.tokenobj.functions.symbol().call()

    def decimals(self):
        return self.tokenobj.functions.decimals().call()

    def totalSupply(self):
        return self.tokenobj.functions.totalSupply().call()

    def token_balance(self,owner):
        return self.tokenobj.functions.balanceOf(owner).call()

    def allowance(self,owner,spender):
        return self.tokenobj.functions.allowance(owner,spender).call()

    def new_approve_tx(self,owner,spender,allowance_value,gas_limit):
        tx_data = self.tokenobj.functions.approve(spender, allowance_value).build_transaction({
            'chainId': self.wb3.eth.chain_id, 
            'gas': gas_limit,  
            'gasPrice': self.wb3.eth.gas_price, 
            'nonce': self.wb3.eth.get_transaction_count(owner),
            'from':owner,
        })
        return tx_data

    def new_transfer_tx(self,address_from,to,amount,gas_limit):
        tx_data = self.tokenobj.functions.transfer(to, amount).build_transaction({
            'chainId': self.wb3.eth.chain_id, 
            'gas': gas_limit,  
            'gasPrice': self.wb3.eth.gas_price, 
            'nonce': self.wb3.eth.get_transaction_count(address_from),
            'from':address_from,
        })
        return tx_data

    def new_transferFrom_tx(self,spender,owner,to,amount,gas_limit):
        tx_data = self.tokenobj.functions.transferFrom(owner,to, amount).build_transaction({
            'chainId': self.wb3.eth.chain_id, 
            'gas': gas_limit,  
            'gasPrice': self.wb3.eth.gas_price, 
            'nonce': self.wb3.eth.get_transaction_count(spender),
            'from':spender,
        })
        return tx_data



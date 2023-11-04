class ERC20:
    def __init__(self,wb3,tokenobj):
        self.wb3 = wb3
        self.tokenobj = tokenobj
    
    def symbol(self):
        return self.tokenobj.functions.symbol().call()

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

    def new_transferFrom_tx(self,address_from,to,amount,gas_limit):
        tx_data = self.tokenobj.functions.transferFrom(address_from,to, amount).build_transaction({
            'chainId': self.wb3.eth.chain_id, 
            'gas': gas_limit,  
            'gasPrice': self.wb3.eth.gas_price, 
            'nonce': self.wb3.eth.get_transaction_count(address_from),
            'from':address_from,
        })
        return tx_data



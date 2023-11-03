import re
from dotenv import load_dotenv
import os

load_dotenv()

gas_limit = int(os.getenv('Gas_Limit'))

def token_balance(tokenobj,owner):
    return tokenobj.functions.balanceOf(owner).call()

def allowance(tokenobj,owner,spender):
    return tokenobj.functions.allowance(owner,spender).call()

def new_approve_tx(tokenobbj,wb3,owner,spender,allowance_value):
    tx_data = tokenobbj.functions.approve(spender, allowance_value).build_transaction({
        'chainId': wb3.eth.chain_id, 
        'gas': gas_limit,  
        'gasPrice': wb3.eth.gas_price, 
        'nonce': wb3.eth.get_transaction_count(owner),
        'from':owner,
    })
    return tx_data



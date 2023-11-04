from dotenv import load_dotenv
import os

load_dotenv()

gas_limit = int(os.getenv('Gas_Limit'))

def new_feed_tx(wb3,contractobj,address_from,info,amount): 
    tx_data =  contractobj.functions.feed(info,amount).build_transaction({
        'chainId': wb3.eth.chain_id,  
        'gas': gas_limit,
        'gasPrice': wb3.eth.gas_price,
        'nonce': wb3.eth.get_transaction_count(address_from),   
        'from':address_from, 
    })
    return tx_data



 




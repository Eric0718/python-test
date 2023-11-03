def sendSignTx(wb3,contractobj,address_from,amount,private_key): 
    # 创建交易
    gas_price = wb3.eth.gas_price
    gas_limit = 300000
    tx = contractobj.functions.feed('buyfood',amount).build_transaction({
        'chainId': wb3.eth.chain_id,  
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': wb3.eth.get_transaction_count(address_from),   
        'from':address_from, 
    })

    try:
        estGas = wb3.eth.estimate_gas(tx)    
    except Exception as e:
        print("Transaction error:",e)
        return False

    if estGas > wb3.eth.get_balance(address_from):
        print("Insufficient gas balance.")
    signTx = wb3.eth.account.sign_transaction(tx, private_key)
    hash = wb3.eth.send_raw_transaction(signTx.rawTransaction)
    print("Transaction sent with hash:", hash.hex())
    return hash.hex()
        

 




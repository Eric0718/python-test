
def isApproved(tokenobj,owner,spender,allowance_amount):
    allowance_value = tokenobj.functions.allowance(owner,spender).call()
    print("allowance_value:",allowance_value)

    if allowance_value < allowance_amount:
        print("Insufficient allowance value.")
        return False
        
    return True

def approve(tokenobbj,wb3,address_from,spender,allowance_value,gas_limit,private_key):
    tx_data = tokenobbj.functions.approve(spender, allowance_value).build_transaction({
        'chainId': wb3.eth.chain_id, 
        'gas': gas_limit,  # 根据需要调整
        'gasPrice': wb3.eth.gas_price,  # 根据需要调整
        'nonce': wb3.eth.get_transaction_count(address_from),
        'from':address_from,
    })

    try:
        estGas = wb3.eth.estimate_gas(tx_data)
    except Exception as e:
        print("approve estimate_gas error:",e)
        return False

    if estGas > wb3.eth.get_balance(address_from):
        print("approve Insufficient balance.")
        return False
    
    try:
        signTx = wb3.eth.account.sign_transaction(tx_data, private_key)
        hash = wb3.eth.send_raw_transaction(signTx.rawTransaction)
        print("Transaction sent with hash:", hash.hex())
    except Exception as e:
        print("send_raw_transaction error:",e)
        return False
    return True


from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import erc20

load_dotenv()
nodeUrl_test = os.getenv('Bsc_Url_Test')
contractAddr = os.getenv('Contract_Address')
token_address = os.getenv('Token_Address')

# 您的钱包地址和私钥
address_from = os.getenv('Test_Address')
private_key = os.getenv('Priv_Key')
address_to = "0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE"

# 合约ABI
with open('/Users/lzl/work/python/contact/abi/BDB.abi','r') as BDBABI:
    contract_abi = json.load(BDBABI)

with open('/Users/lzl/work/python/contact/abi/ERC20.abi','r') as erc20ABI:
    erc20_abi = json.load(erc20ABI)

# 连接到Ethereum节点
wb3 = Web3(Web3.HTTPProvider(nodeUrl_test))

# 确保连接成功
if wb3.is_connected() != True:
    sys.exit()

# 创建交易
gas_price = wb3.eth.gas_price
gas_limit = 300000

contractobj = wb3.eth.contract(address=contractAddr, abi=contract_abi)
tokenobj = wb3.eth.contract(address=token_address, abi=erc20_abi)


buy_amount = 1000000000000000000

allowance_value = tokenobj.functions.allowance(address_from,contractAddr).call()
print("allowance_value:",allowance_value)

if allowance_value < buy_amount:
    print("Insufficient allowance value.")
    """  if erc20.approve(tokenobj,wb3,address_from,contractAddr,buy_amount,gas_limit,private_key) != True:
        print("approve failed.") """

tx = contractobj.functions.feed('buyfood',buy_amount).build_transaction({
    'chainId': wb3.eth.chain_id,  
    'gas': gas_limit,
    'gasPrice': gas_price,
    'nonce': wb3.eth.get_transaction_count(address_from),   
    'from':address_from, 
})

try:
    estGas = wb3.eth.estimate_gas(tx)
    if estGas > wb3.eth.get_balance(address_from):
        print("Insufficient gas balance.")
    signTx = wb3.eth.account.sign_transaction(tx, private_key)
    hash = wb3.eth.send_raw_transaction(signTx.rawTransaction)
    print("Transaction sent with hash:", hash.hex())
except Exception as e:
    print("Transaction error:",e)
        

 




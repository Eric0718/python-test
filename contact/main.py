from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import erc20
import send_tx

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

contractobj = wb3.eth.contract(address=contractAddr, abi=contract_abi)
tokenobj = wb3.eth.contract(address=token_address, abi=erc20_abi)
amount = 1000000000000000000

def main():
    erc20.isApproved(tokenobj,address_from,contractAddr,amount)
    send_tx.sendSignTx(wb3,contractobj,address_from,amount,private_key)

if __name__ == "__main__":
    main()
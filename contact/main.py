from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import erc20
import send_tx
import argparse

load_dotenv()
nodeUrl_test = os.getenv('Bsc_Url_Test')
contractAddr = os.getenv('Contract_Address')
token_address = os.getenv('Token_Address')
gasLimit = int(os.getenv('Gas_Limit'))

address_from = os.getenv('Test_Address')
private_key = os.getenv('Priv_Key')
address_to = "0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE"

with open('/Users/lzl/work/python/contact/abi/BDB.abi','r') as BDBABI:
    contract_abi = json.load(BDBABI)

with open('/Users/lzl/work/python/contact/abi/ERC20.abi','r') as erc20ABI:
    erc20_abi = json.load(erc20ABI)

wb3 = Web3(Web3.HTTPProvider(nodeUrl_test))

if wb3.is_connected() != True:
    sys.exit()

contractobj = wb3.eth.contract(address=contractAddr, abi=contract_abi)
tokenobj = wb3.eth.contract(address=token_address, abi=erc20_abi)

def allowance():
    allowanceValue = erc20.allowance(tokenobj,address_from,contractAddr)
    print(f"allowance value: {allowanceValue}")

def approve(amount):
    txdata = erc20.new_approve_tx(tokenobj,wb3,address_from,contractAddr,amount)
    try:
        send_tx.send_sign_tx(wb3,txdata,address_from,private_key)
    except Exception as e:
        print("sendSignTx error:",e)

def buy_food(amount):
    txdata = send_tx.new_feed_tx(wb3,contractobj, address_from,'buy_food',amount)
    try:
        send_tx.send_sign_tx(wb3,txdata,address_from,private_key)
    except Exception as e:
        print("sendSignTx error:",e)

def main(args):
    amount = 1000000000000000000
    if args.option == 'allowance':
        allowance()
    elif args.option == 'approve':
        approve(amount)
    elif args.option == 'buy_food':
        buy_food(amount)
    elif args.option == 'balanceOf':
        print(f'{address_from} token balance:{erc20.token_balance(tokenobj,address_from)}')
    else:
        print(f"user -h or --help to get some help.")

if __name__ == "__main__":
    help_str = """ option: 
    allowance 查看授权；
    approve 授权；
    buy_food 买猫粮
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--option",type=str,help=help_str)
    args = parser.parse_args()
    main(args)
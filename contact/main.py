from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import ERC20 as erc
import petcat as cat
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

def send_sign_tx(wb3,txdata,address_from,private_key):
    estGas = wb3.eth.estimate_gas(txdata)
    if estGas > wb3.eth.get_balance(address_from):
        print("Insufficient gas balance.")

    signTx = wb3.eth.account.sign_transaction(txdata, private_key)
    hash = wb3.eth.send_raw_transaction(signTx.rawTransaction)
    print("Transaction sent with hash:", hash.hex())
    return hash.hex()
        

def main(args):    
    erc20 = erc.ERC20(wb3,tokenobj)
    if args.option == 'allowance':
        allowanceValue = erc20.allowance(address_from,contractAddr)
        print(f"allowance value: {allowanceValue}")
    elif args.option == 'symbol':
        symbol = erc20.symbol()
        print(f'symbol: {symbol}')
    elif args.option == 'approve':
        approve_amount = 1000000000000000000
        txdata = erc20.new_approve_tx(address_from,contractAddr,approve_amount,gasLimit)
        try:
            send_sign_tx(wb3,txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'buy_food':
        amount = 1000000000000000000
        txdata = cat.new_feed_tx(wb3,contractobj, address_from,'buy_food',amount)
        try:
            send_sign_tx(wb3,txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'balanceOf':
        balance = erc20.token_balance(address_from)
        print(f'{address_from} token balance:{balance}')
    elif args.option == 'transfer':
        to = '0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE'
        amount = 2000000000000000000
        txdata = erc20.new_transfer_tx(address_from,to,amount,gasLimit)
        try:
            send_sign_tx(wb3,txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'transferFrom':
        addr_from = ''
        to = '0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE'
        amount = 2000000000000000000
        txdata = erc20.new_transferFrom_tx(addr_from,to,amount,gasLimit)
        try:
            send_sign_tx(wb3,txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
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
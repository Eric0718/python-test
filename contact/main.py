import os
import ERC20 
import petcat 
import argparse
from dotenv import load_dotenv

load_dotenv()

token_address = os.getenv('Token_Address')
chainRpcUrl = os.getenv('Bsc_Rpc_Url_Test')
cat_contract = os.getenv('Contract_Address')
gasLimit = int(os.getenv('Gas_Limit'))
address_from = os.getenv('Test_Address')
private_key = os.getenv('Priv_Key')
address_to = "0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE"

catAbi = '/Users/lzl/work/python/contact/abi/CAT.abi'
erc20Abi = '/Users/lzl/work/python/contact/abi/ERC20.abi'

def main(args):    
    erc20 = ERC20.ERC20(erc20Abi,chainRpcUrl,token_address)
    cat = petcat.Petcat(catAbi,chainRpcUrl,cat_contract)

    if args.option == 'allowance':
        allowanceValue = erc20.allowance(address_from,cat_contract)
        print(f"allowance value: {allowanceValue}")
    elif args.option == 'tokeninfo':
        print(f'symbol: {erc20.symbol()}')
        print(f'decimals: {erc20.decimals()}')
        print(f'totalSupply: {erc20.totalSupply()}')
    elif args.option == 'approve':
        owner = address_from
        spender = cat_contract #"0x06a2f352983c400a57AB00752d651a6fc2A3Ff2b"
        approve_amount = 100000000000000000000
        
        try:
            txdata = erc20.new_approve_tx(owner,spender,approve_amount,gasLimit)
            erc20.send_sign_tx(txdata,owner,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'buy_food':
        amount = 1000000000000000000
        try:
            txdata = cat.new_feed_tx(address_from,'buy_food',amount,gasLimit)
            cat.send_sign_tx(txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'buy_nft':
        amount = 1000000000000000000
        try:
            txdata = cat.new_buyNft_tx(address_from,'buy_food',amount,gasLimit)
            cat.send_sign_tx(txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'balanceOf':
        balance = erc20.token_balance(address_from)
        print(f'{address_from} token balance:{balance}')
    elif args.option == 'transfer':
        to = '0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE'
        amount = 2000000000000000000
        
        try:
            txdata = erc20.new_transfer_tx(address_from,to,amount,gasLimit)
            erc20.send_sign_tx(txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'transferFrom':
        owner = '0x1bE0D2F17c64b9b3F0dAc972d16001EDE7cd0bfE'
        to = '0x9DAC6fB1dF05b8390dcE0221A60aF06C8383a530'
        amount = 20000000000000000
        
        try:
            txdata = erc20.new_transferFrom_tx(address_from,owner,to,amount,gasLimit)
            erc20.send_sign_tx(txdata,address_from,private_key)
        except Exception as e:
            print("sendSignTx error:",e)
    elif args.option == 'config':
        print(f"erc20:{erc20.getConfig()}")
        print(f"cat:{cat.getConfig()}")
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
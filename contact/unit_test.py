import unittest
import petcat
from dotenv import load_dotenv
import os

load_dotenv()

class TestPetcat(unittest.TestCase):
    def setUp(self):
        self.owner = os.getenv('Test_Address')
        self.private_key = os.getenv('Priv_Key')
        self.gasLimit = int(os.getenv('Gas_Limit'))
        self.amount = 1000000000000000000
        self.abifile = '/Users/lzl/work/python/contact/abi/CAT.abi'
        self.chainUrl = 'https://bsc-testnet-dataseed.bnbchain.org'
        self.cat_contrat = '0x1051087c014d4567FAEdD30FA557cbb8F7482d9b'
        self.cat = petcat.Petcat(self.abifile,self.chainUrl,self.cat_contrat)

    def test_NewInstance(self):        
        url,cat_addr = self.cat.getConfig()
        self.assertEqual(self.chainUrl,url)
        self.assertEqual(self.cat_contrat,cat_addr)
        self.assertTrue(self.cat.isWeb3Connected())
        print(f'test NewInstance ok!')

    def test_send_feed_tx(self):
        try:
            txdata = self.cat.new_feed_tx(self.owner,'buy_food',self.amount,self.gasLimit)
            hash = self.cat.send_sign_tx(txdata,self.owner,self.private_key)
        except ValueError as e:
            print("test_send_feed_tx error:",e)
        else:
            print(f'test_send_feed_tx hash:{hash}')
    """ def test_send_buyNft_tx(self):
        try:
            txdata = self.cat.new_buyNft_tx(self.owner,'buy_nft',self.amount,self.gasLimit)
            hash = self.cat.send_sign_tx(txdata,self.owner,self.private_key)
        except ValueError as e:
            print("test_send_buyNft_tx error:",e)
        else:
            print(f'test_send_buyNft_tx hash:{hash}') """
import unittest
import petcat
from dotenv import load_dotenv
import os

load_dotenv()

class TestPetcat(unittest.TestCase):
    __owner = os.getenv('Test_Address')
    __private_key = os.getenv('Priv_Key')
    __gasLimit = int(os.getenv('Gas_Limit'))
    __amount = 1000000000000000000
    

    def test_NewInstance(self):
        abifile = '/Users/lzl/work/python/contact/abi/CAT.abi'
        chainUrl = 'https://bsc-testnet-dataseed.bnbchain.org'
        cat_contrat = '0x1051087c014d4567FAEdD30FA557cbb8F7482d9b'
        
        cat = petcat.Petcat(abifile,chainUrl,cat_contrat)

        url,cat_addr = cat.getConfig()

        self.assertEqual(chainUrl,url)
        self.assertEqual(cat_contrat,cat_addr)
        self.assertTrue(cat.isWeb3Connected())
        
        self.cat = cat
    
    def test_send_feed_tx(self):
        txdata = self.cat.new_feed_tx(self.__owner,'buy_food',self.__amount,self.__gasLimit)
        self.cat.send_sign_tx(txdata,self.__owner,self.__private_key)
    
    def test_send_buyNft_tx(self):
        txdata = self.cat.new_buyNft_tx(self.__owner,'buy_nft',self.__amount,self.__gasLimit)
        self.cat.send_sign_tx(txdata,self.__owner,self.__private_key)
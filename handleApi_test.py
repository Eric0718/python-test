import argparse
import requests
import json

# 目标URL
BaseUrl = "https://www.petcat.pro/petcat-test/api/HandlePublic"

def BaseRequest(url,http_method ,params):
    print("Test method {} start >>>>>>:".format(params['method']))
    # 发起带参数的HTTP GET请求
    if http_method == 'post':
        res = requests.post(url, params=params)
    elif http_method == 'get':
        res = requests.get(url, params=params)
    else:
        print(f"\tUnsupported http method: {http_method}")
        return
    # 检查响应状态码
    if res.status_code == 200:
        # 在这里可以对响应内容进行处理
        data = res.json()
        if data['response']['errCode'] == 0:
            print("\tresponse data:",data['response']['data'])
        else:
            print("\tresponse error ====== code: {}, msg: {}.".format(data['response']['errCode'],data['response']['msg']))
    else:
        print(f"\thttp request failed，code: {res.status_code}")
    
    print("Test method {} end <<<<<<.\n".format(params["method"]))

def BaseRequest_JsonData(url,http_method,json_data):
    header = {"Content-Type": "application/json"}
    # 发起带参数的HTTP GET请求
    if http_method == 'post':
        res = requests.post(url, data=json_data,headers=header)
    elif http_method == 'get':
        res = requests.get(url, data=json_data,headers=header)
    else:
        print(f"\tUnsupported http method: {http_method}")
        return
    # 检查响应状态码
    if res.status_code == 200:
        # 在这里可以对响应内容进行处理
        data = res.json()
        print("\trequest data:",data)
    else:
        print(f"\thttp request failed, code: {res.status_code}")
    
    print("Test end <<<<<<.\n")

def Test_user_cat_batch():
    # 参数字典
    method = "user_cat"
    option = 'batch'
    params = {
        "method":method,
        "option":option,
        "addr":"0xD53e57d60Bcf0bD35170969Cbc42E052e5b65f97",
        "page":0,
        "limit":10
    }
    BaseRequest(BaseUrl,'post',params)

def Test_user_cat_zero():
    # 参数字典
    method = "user_cat"
    option = 'batch'
    params = {
        "method":method,
        "option":option,
        "addr":"0xD53e57d60Bcf0bD35170969Cbc42E052e5b65f97",
        "page":0,
        "limit":10
    }
    BaseRequest(BaseUrl,'post',params)

def Test_feed_cat():
    # 参数字典
    method = "feed_cat"
    option = 'batch'
    params = {
        "method":method,
        "option":option,
        "addr":"0xD53e57d60Bcf0bD35170969Cbc42E052e5b65f97",
        "page":0,
        "limit":10,
        "flag":0
    }
    BaseRequest(BaseUrl,'post',params)

def Test_store_list():
    # 参数字典
    method = "store_list"
    option = 'list'
    params = {
        "method":method,
        "option":option,
        "page":0,
        "limit":10,
        "flag":0
    }
    BaseRequest(BaseUrl,'post',params)

def Test_token_price():
    # 参数字典
    method = "token_price"
    option = 'cat'
    params = {
        "method":method,
        "option":option,
    }
    BaseRequest(BaseUrl,'post',params)

    option = 'bnb'
    params = {
        "method":method,
        "option":option,
    }
    BaseRequest(BaseUrl,'post',params)

def Test_get_originbill():
    # 参数字典
    method = "get_originbill"
    option = 'active'
    params = {
        "method":method,
        "option":option,
        "addr":'0xD53e57d60Bcf0bD35170969Cbc42E052e5b65f97',
        "page":0,
        "limit":10,
    }
    BaseRequest(BaseUrl,'post',params)

def Test_tx_record():
    # 参数字典
    method = "tx_record"
    params = {
        "method":method,
        "addr":'0xD53e57d60Bcf0bD35170969Cbc42E052e5b65f97',
        "page":0,
        "limit":10,
    }
    BaseRequest(BaseUrl,'post',params)

def Test_get_nodes():
    # 参数字典
    method = "get_nodes"
    params = {
        "method":method,
    }    
    BaseRequest(BaseUrl,'post',params)

def Test_json_data():
    data = {
        "userId": "John",
        "extra": 30,
        "transId": "New York",
        "sign":"sign"
    }

    # 将 JSON 数据转换为字符串
    json_data = json.dumps(data)

    url = "https://www.petcat.pro/petcat-test/api/PetcatAd"
    print("Test method {} start >>>>>>:".format('Test_json_data'))
    BaseRequest_JsonData(url,'post',json_data)

def main(args):
    if args.test == 'Test_user_cat_batch':
        Test_user_cat_batch()
    elif args.test == 'Test_user_cat_zero':
        Test_user_cat_zero()
    elif args.test == 'Test_feed_cat':
        Test_feed_cat()
    elif args.test == 'Test_store_list':
        Test_store_list()
    elif args.test == 'Test_token_price':
        Test_token_price()
    elif args.test == 'Test_get_originbill':
        Test_get_originbill()
    elif args.test == 'Test_tx_record':
        Test_tx_record()
    elif args.test == 'Test_get_nodes':
        Test_get_nodes()
    elif args.test == 'Test_json_data':
        Test_json_data()
    elif args.test_all:
        Test_user_cat_batch()
        Test_user_cat_zero()
        Test_feed_cat()
        Test_store_list()
        Test_token_price()
        Test_get_originbill()
        Test_tx_record()
        Test_get_nodes()
    else:
        print(f"user -h or --help to get some help.")

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_all",action="store_true",help="执行全部测试")
    parser.add_argument("--test",type=str,help="执行单个测试")
    args = parser.parse_args()
    main(args)

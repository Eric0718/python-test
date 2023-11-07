import httpx
""" 调用 httpx 包"""

#url = "https://spa16.scrape.center/"

url = "https://www.httpbin.org/get"
hds = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; ONEPLUS A3010 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 BingWeb/6.9.0'
}

res = httpx.get(url,headers=hds)
print(res.status_code,res.headers)

print(res.text)

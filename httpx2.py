from distutils.log import error
import httpx

""" 开启 http2 """

url = "https://spa16.scrape.center/"
cli = httpx.Client(http2=True) 

res = cli.get(url)
print(res.status_code,"===========\n")

url1 = "https://spa16.scrape.center/"
with httpx.Client(http2=True) as clit:
    res = clit.get(url1)
    print(res,"===========\n")


client = httpx.Client(http2=True) 
try:
    res = client.get(url)
    print(res,res.http_version,"===========\n")
except error.URLError as e:
    print(e.reason)

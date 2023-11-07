""" 调用 requests 包 """
import requests
import re
from os.path import exists
from os import makedirs

RESULTS_DIR = './results/picture'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

#get抓取页面内容，配合正则表达式
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
r = requests.get('https://ssr1.scrape.center/',headers=headers)
#print(r.text)
print("=========================")
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
print("++++++++++++++++++++++++")

#get抓取二进制，图片，音频，视频
r2 = requests.get('https://scrape.center/favicon.ico')
#print(r2.text)
#print(r2.content) 
with open('./results/picture/favicon.ico','wb') as f:
    f.write(r2.content)
print("-----------------------")

#post请求
data = {'name':'germy','age':'25'}
res = requests.post("https://www.httpbin.org/post",data=data)
print(res.text)

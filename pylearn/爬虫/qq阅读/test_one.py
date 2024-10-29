import requests

from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

url = 'https://book.qq.com/book-read/48087169/3'
response = requests.get(url,headers=header)

# 得到的网页的HTML文件
soup = BeautifulSoup(response.text,'lxml')
elements = soup.select('div#article p')
with open('./result/one.text','w') as f:
    for e in elements:
        f.write(e.text)

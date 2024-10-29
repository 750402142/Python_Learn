from idlelib.colorizer import prog_group_name_to_tag

import requests

from bs4 import BeautifulSoup

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
url = 'https://book.qq.com/api/book/detail/chapters?bid=48087169'
response = requests.get(url,headers=header)
data = response.json()
for i in data['data']:
    cid = i['cid']
    chaName = i['chapterName']
    url = f'https://book.qq.com/book-read/48087169/{cid}'
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    elements = soup.select('div#article p')
    with open(f'./result/{chaName}.txt','w') as f:
        for e in elements:
            f.write(e.text)


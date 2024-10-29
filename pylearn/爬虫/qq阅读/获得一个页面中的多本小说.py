from idlelib.colorizer import prog_group_name_to_tag

import requests

from bs4 import BeautifulSoup
import os
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
# 可以获得全部小说的url
response = requests.get('https://book.qq.com/book-rank/male-sell',headers = header)
soup = BeautifulSoup(response.text,'lxml')
elements = soup.select('div.book-large.rank-book')
for element in elements:
    bid = element['mulan-bid']
    print('开始下载:'+bid)
    if not os.path.exists(bid):
        os.makedirs(bid)
    # 获得某一部小说的url
    url = f'https://book.qq.com/api/book/detail/chapters?bid={bid}'
    response = requests.get(url,headers = header)
    for i in  response.json()['data']:
        cid = i['cid']
        chaName = i['chapterName']
        # 获得某一部小说章节的url
        url = f'https://book.qq.com/book-read/{bid}/{cid}'
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, 'lxml')
        elements = soup.select('div#article p')
        with open(f'./{bid}/{chaName}.txt', 'w') as f:
            for e in elements:
                f.write(e.text)
        print('下载成功'+chaName)

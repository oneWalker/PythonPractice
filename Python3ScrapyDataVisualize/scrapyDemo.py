#一个简单的爬虫的例子：
import requests
import json
import re
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
proxies = {
    'http':"http://10.0.0.10:3128",
    'https':"http://10.0.0.10:1080",
}
strhtml = requests.get(url,headers=headers)
soup = BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
  result = {
      'title':item.get_text(),
      'link':item.get('href'),
      'ID':re.findall('\d+',item.get('href'))
  }
  print(result)
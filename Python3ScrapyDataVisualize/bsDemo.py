#爬虫并解析天气
import requests
import time
import json
url = 'https://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
data = strhtml.text
data = data.split("\n")
for i in range(3):
  data.remove(data[0])
loopCount = 0;
for item in data:
  if(loopCount>5):
    break
  url = 'https://devapi.qweather.com/v7/weather/3d?location='+item[2:13]+'&key=f888505037cc4f7b9eaf7ac26ae997d9'
  strhtml = requests.get(url)
  time.sleep(1)
  dic = strhtml.json()
  loopCount += 1;
  if(dic['code'] == '200'):
    for daily in dic['daily']:
      print(daily['tempMax'])
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:51:03 2017

@author: LIU
"""

import requests,re,time
from bs4 import BeautifulSoup
count = 0
i = 0
sum,count_s = 0,0
while(count<50):
    try:
        r=requests.get('http://book.douban.com/subject/2174013/comments/hot?p='+str(i+1))
    except Exception as err:
        print(err)
        break
    soup=BeautifulSoup(r.text,'lxml')
    comments=soup.find_all('p','comment-content')
    for item in comments:
        count=count+1
        if count>50:
            break
        print(count)
        print(item.string)
    
    #进行评分筛选的匹配模式
    pattern=re.compile('<span class="user-stars allstar(.*?)rating"')
    #获取分数模型
    p=re.findall(pattern,r.text)
    
    for star in p:
        count_s=count_s+1
        sum+=int(star)
        print("rating"+star)
    time.sleep(5)#delay request
    i+=1
    if count >= 50:
        print(sum/count_s)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: LIU
"""
import pandas as pd
#从文件中读取数据并存入dataframe结构中
ratingData=pd.read_table(r"C:\Users\LIU\Downloads\ml-100k\u.data",sep='\t',names=['userid','itemid','rating','timestamp'],usecols=['userid','itemid','rating'])
#print(ratingData.groupby('userid').size())
userData=pd.read_table(r"C:\Users\LIU\Downloads\ml-100k\u.user",sep='|',names=['userid','age','gender','ocuppation','zipcode'],usecols=['userid','gender','age'])
merggData=pd.merge(ratingData,userData,on='userid')

meanDataM=merggData[merggData.gender=='M'].groupby('userid').rating.mean().std()
meanDataF=merggData[merggData.gender=='F'].groupby('userid').rating.mean().std()

#将结果存入文本文档
with open(r'C:\Users\LIU\Downloads\movieresult.txt','w') as f:
    f.write("{:.0f}{:.0f}".format(meanDataM*100, meanDataF*100) )
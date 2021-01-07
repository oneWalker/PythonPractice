# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: LIU
"""
import numpy as np
list1=[88.0,74.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]
#使用sklearn中的方法
from sklearn.cluster import KMeans
X=np.array([list1,list2,list3,list4,list4,list5,list6])
Kmeans=KMeans(n_clusters=2).fit(X)
pred=Kmeans.predict(X)
print(pred)
#使用scipy中的方法进行kmeans
from scipy.cluster.vq import vq,kmeans,whiten
data=np.array([list1,list2,list3,list4,list5,list6])
#计算每个数据的方差
whiten=whiten(data)
#将两类方差进行区分
centroids,_=kmeans(whiten,2)
result,_=vq(whiten,centroids)
print (result)

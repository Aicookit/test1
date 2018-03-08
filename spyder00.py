#!/bin/env python
#_*_ coding:utf-8 _*_
'''
created on 2018年1月16日
@author:yingming
'''
import re
import urllib.request
def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    # print(type(html))
    html=html.decode('utf-8')
    # print(html)
    return
def getImg(html):
    reg=r'img srcset="(.+?\.jpg)"'
    imgre=re.compile(reg)
    # print(type(imgre))
    # print(imgre)
    imglist=re.findall(imgre,html)
    print(type(imglist))
    print(imglist)
    # num=0
    # for imgurl in imglist:
    #     urllib.request.urlretrieve(imgurl,'D:\img\free%s.jpg' %num)
    #     num+=1


html=getHtml('http://www.pixabay.com/zh/')
print(getImg(html))


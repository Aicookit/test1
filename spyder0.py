#!/bin/env python
# -*- coding:utf-8 -*-
'''
created on 2017年12月18日
@author:yingming
'''
'''
爬取Python贴吧里面用户名及头像图片信息.
爬取网页链接:http://tieba.baidu.com/p/5480261753
只需要爬取该贴吧链接里面的头像即可,用户名作为头像图片的名称。
'''
#导入模块
import urllib
import re
import os
import glob

#抓取页数
page_amount=5

#抓取首页html代码
def get_page(url):
    req=urllib.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    response=urllib.urlopen(req)
    html=response.read().decode('utf-8')
    return html

#抓取图片
def read_image(url):
    req=urllib.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    response = urllib.urlopen(url)
    html = response.read()
    return html

#d得到图片列表
def get_pictures_url_list(url):
    html=get_page()
    i=re.findall(r'<img username=(>*?)/></a>.*?<a data-field=.*?>(.*?)</a>',re.S)




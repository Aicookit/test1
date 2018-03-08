#!/user/bin/env python
# _*_ coding: utf_8 _*_
'''
created on 2017年11月18日

@author:yingming
'''
import urllib.request
response = urllib.request.urlopen('http://www.maiziedu.com/course/teachers/')
print(response.read())
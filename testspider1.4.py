#!/user/bin/env python
#coding:utf-8
'''
Created on 2017年11月16日

@author:yingming
'''
import urllib2
import re
import os
print('开始抓取...')

for i in range(1,28):

    url= "http://www.maiziedu.com/course/teachers/?page'+str(i)+"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    headers={ 'User-Agent': user_agent }
    try:
        request=urllib2.Request(url,headers=headers)
        response=urllib2.urlopen(request)
        content = response.read()
    except urllib2.HTTPError as e:
        print e
    except urllib2.URLError as e:
        print e
        exit
    pattern = re.compile('<p class.*?>(.*?).*?<a href=.*?>(.*?)</p>',re.S)

    items = re.findall(pattern,content)
    print items
    for item in items:
        item_new = item[1]
        path="teacher"
        if not os.path.exists(path):
            os.makedirs(path)
        file_path=path+'/'+item[0]+'.txt'
        f=open(file_path,'w')
        f.write(item_new)
        f.close
print('抓取完了！')


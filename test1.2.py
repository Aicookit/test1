#-*-coding:utf-8-*-
import urllib
import re
import os

class spider00:

    def __init__(self, root_url, pattern, deep_index=1, file_path='./'):
    self.url = url
    self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

    def get_html(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

    def get_data(html):
    data = re.compile(r'<img username="(.*?)" class="" src="(.*?)"/></a>',re.S)
    data_list=re.findall(data,html)
    return data_list
#头像传入用户名目录
#头像和用户名保存


print get_data(html)
    if __name__ == '__main__':
    html = get_html('http://tieba.baidu.com/p/5394856726')
    spider0 = spider00(url, baike_regex, deep_index=2, file_path='./bak/')
    spider0.run()


import os
import re

import requests


class BaiduSpider(object):
    def __init__(self):
        self.base_url = "http://tieba.baidu.com"

    def getIndex(self):
        req = requests.get(self.base_url + '/f?kw=python&fr=ala0&tpl=5')
        content = req.text
        pattern = re.compile(r'<a href="(.*?)".*?class="j_th_tit')
        return re.findall(pattern, content)

    def indexDown(self, index_url):
        req = requests.get(index_url)
        print("the url is " + index_url)
        content = req.text
        pattern = re.compile('<ul class="p_author".*?<img username="(.*?)".*?src="(.*?)"', re.S)
        return re.findall(pattern, content)

    def saveImg(self, down_url):
        path = 'tiebaUser'
        if not os.path.exists(path):
            os.makedirs(path)
        print(down_url)
        data = requests.get(down_url[1], stream=True)
        with open(path + '/' + down_url[0] + '.jpg', 'wb') as f:
            for chunk in data.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    def run(self):
        index_list = self.getIndex()
        if index_list:
            for index_url in index_list:
                down_list = self.indexDown(self.base_url + index_url)
                self.saveImg(down_list[0])


if __name__ == '__main__':
    spider = BaiduSpider()

    spider.run()


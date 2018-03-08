#!bin/env/python3
#_*_ coding:utf-8 _*_
# created on 22/1/2018
# @author:Yingming
# email:642250219@qq.com

import requests,re,os

class tiebaSpider(object):
    def __init__(self):
        self.base_url='http://tieba.baidu.com'

    def getIndex(self):
        req=requests.get(self.base_url+'/f?kw=python&fr=ala0&tpl=5')#网址为什么分开写呢？ content=req.text#此处为什么要用text方法？
        pattern=re.compile(r'<a href="(.*?)".*?class="j_th_tit "')#<a （rel="noreferrer"：正则时为啥这里可以直接省略？） href="{/p/5461033838" title="为啥这部分也能放入到（.*?）中？不是应该只取后面标题段文字吗？}想转行做Python，如何学习比较好".*?class="j_th_tit "
        return re.findall(pattern,content)#参数顺序为什么是这样？而不是(content,pattern)

    def downIndex(self,index_url):#传入的第二个参数有什么作用？
        req=requests.get(index_url)#index_url参数并没有赋值（像上面的base_url至少知道请求的网址，而这里好像没有赋值）
        print('the url is'+index_url)#为什么要print出来？这行代码写出来表示什么？
        content=req.text
        pattern=re.compile('<ul class="p_author".*?<img username="(.*?)".*?src="(.*?)"',re.S)
        return re.findall(pattern,content)

    def saveFile(self,down_url):#参数为什么要用down_url?如第19行所问。
        path='tiebaUser'#运行程序后并没有看到有tiebaUser的文件夹被创建，也没看到爬取得东西？
        if not os.path.exists(path):
            os.makedirs(path)
        print(down_url)#这里为什么也要print出来？
        data=requests.get(down_url[1],stream=True)
        with open(path+'/'+'down_url[0]'+'.jpg','wb')as f:
            for chunk in data.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
#对下面的run对象运行的思路有点混乱，需要老师讲解一下它的运行过程
    def run(self):
        index_list=self.getIndex()
        if index_list:
            for index_url in index_list:
                down_list=self.downIndex(self.base_url+index_url)
                self.saveFile(down_list[0])

if __name__=="__main__":
    spider=tiebaSpider()
    spider.run()
#运行后好像没有文件被爬取下来，文件名tiebaUser也没被创建？





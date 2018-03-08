#!/user/bin/env python
#coding:utf-8
'''
Created on 2017年11月16日

@author:yingming
'''
import random
class colorball:
    redballqty=0
    blueballqty=0
    redmax=0
    bluemax=0
    ballrecord=()
    def__init__(self,redmax,redqty,bluemax,blueqty):
        self.redmax=redmax
        self.redqty=redqty
        self.bluemax=bluemax
        self.bluemax=bluemax
    def pruduce_new(self):
        redballist=range(1,self.redmax+1)
        rednewlist=random.sample(redballist,self.redqty)
        rednewlist=sorted(rednewlist)

        blueballist=range(1,self.bluemax+1)
        bluenewlist=random.sample(blueballist,self.blueqty)
        self.ballrecord=rednewlist+bluenewlist
def show_result(self):
    print self.ballrecord


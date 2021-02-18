#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/17 下午7:59
# Author : nishizzma
# File : Block.py
import datetime
import hashlib

from NodeMessage import NodeMessage
from NodeMessage import InvalidMessage
from Node import Node
from TraMessage import TraMessage


class Block:
    NUM = 0

    def __init__(self,*args):
        self.messagelist = []  #存储多个交易记录
        self.timestamp = None
        self.hash = None
        self.prev_hash = None
        self.NUM = Block.NUM
        Block.NUM += 1

        if args:
            for arg in args:
                self.add_message(arg)

    def add_message(self, msg):  #增加交易信息
        #区分第一条和后面的  判断是否需要链接
        if len(self.messagelist) > 0:
            msg.link(self.messagelist[-1])
        msg.seal()
        msg.validate()
        self.messagelist.append(msg)

    def link(self, block):  #链接
        self.prev_hash = block.hash

    def seal(self):
        self.timestamp = datetime.datetime.now()
        self.hash = self._hash_block()

    def _hash_block(self):

        return hashlib.sha256((str(self.prev_hash) +
                               str(self.timestamp) +
                               str(self.messagelist[-1].hash)).encode("utf-8")).hexdigest()

    def validate(self):

        for i, msg in enumerate(self.messagelist):
            msg.validate()
            if i > 0 and msg.prev_hash != self.messagelist[i-1].hash:
                raise InvalidBlock("无效block，第{}条交易记录被修改\n".format(i)+ str(self))

        return str(self) + "block ok..."

    def __repr__(self):
        return "===============\nblock = hash:{}\nprehash:{}\nlen:{}\ntime:{}\n==============="\
            .format(self.hash,self.prev_hash,len(self.messagelist),self.timestamp)

class InvalidBlock(Exception):  #异常处理类

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

if __name__ == '__main__':

    try:
        t1 = Node("chaors", "yajun", 999999999)
        t2 = Node("chaors2", "yajun2", 999999999)
        t3 = Node("chaors4", "yajun4", 999999999)

        m1 = NodeMessage(t1)
        m2 = NodeMessage(t2)
        m3 = NodeMessage(t3)

        block = Block(m1, m2, m3)
        block.seal()
        print(block)
        # m1.data = "kkkk"
        block.messagelist[1] = m3
        block.validate()



    except InvalidMessage as e:
        print(e)

    except InvalidBlock as e:
        print(e)





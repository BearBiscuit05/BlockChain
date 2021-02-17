#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/17 下午8:43
# Author : nishizzma
# File : BlockChain.py

from Block import Block
from Block import InvalidBlock
from NodeMessage import NodeMessage
from NodeMessage import InvalidMessage
from Node import Node

class BlockChain:

    def __init__(self):
        self.blocklist = []

    def add_block(self, block):
        if len(self.blocklist) > 0:
            block.prev_hash = self.blocklist[-1].hash
        block.seal()
        block.validate()
        self.blocklist.append(block)

    def validate(self):

        for i, block in enumerate(self.blocklist):
            try:
                block.validate()
            except InvalidBlock as e:
                print(e)
                raise InvalidBlockChain("第{}区块校验错误".format(i))

    def __repr__(self):
        return "BlockChain:{}".format(len(self.blocklist))

class InvalidBlockChain(Exception):  # 异常处理类

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

        block1 = Block(m1, m2, m3)
        block1.seal()



        mychain = BlockChain()
        mychain.add_block(block1)

        print(mychain)


        # #篡改区块
        # block3.messagelist[1] = m33
        # # m31.data = "lkjioh"
        # mychain.validate()

    except InvalidBlockChain as e:
        print(e)
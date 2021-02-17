#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/17 下午8:06
# Author : nishizzma
# File : Transaction.py

import datetime
import hashlib

class Transaction: #新入网结点

    count = 0
    def __init__(self,
                 source_MAC,
                 dis_MAC,
                 source_port,
                 dis_port,
                 data
                 ):
        self.source_MAC = source_MAC
        self.dis_MAC = dis_MAC
        self.source_port = source_port
        self.dis_port = dis_port
        self.data = data
        self.Transaction_id = Transaction.count + 1
        Transaction.count += 1
        self.Transaction_hash = self.hash_workMessage()
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def hash_workMessage(self):
        return hashlib.sha256((str(self.source_MAC) + str(self.source_port) + str(self.dis_MAC) \
                        + str(self.dis_port) + str(self.data)).encode("utf-8")).hexdigest()
    def __repr__(self):

        return "业务信息序号："+str(self.Transaction_id) + "\n业务hash：" \
               + str(self.Transaction_hash) + "\n业务创建时间：" + str(self.timestamp)


if __name__ == '__main__':

    t1 = Transaction("127.2.1.1", "127.1.0.0", "80","403","ababab")
    print(t1)
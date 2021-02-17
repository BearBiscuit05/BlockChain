#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/17 下午6:42
# Author : nishizzma
# File : Node.py


import datetime
import hashlib

class Node: #新入网结点

    def __init__(self,
                 new_node_mac,   #新入网结点MAC地址
                 new_node_ip,   #新入网结点ip地址
                 new_public_key):  #新入网结点公钥
        self.new_node_mac = new_node_mac
        self.new_node_ip = new_node_ip
        self.new_public_key = new_public_key
        self.timestamp = datetime.datetime.now()

    def __repr__(self):

        return "新入网结点MAC地址："+str(self.new_node_mac) + "\n新入网结点IP地址：" + str(self.new_node_ip) + "\n新入网结点公钥："\
               + str(self.new_public_key) + "\n新入网结点入网时间：" + str(self.timestamp)


if __name__ == '__main__':

    t1 = Node("chaors", "127.1.0.0", "stringinginging")
    print(t1)
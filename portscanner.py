#! /usr/bin/python
# -*- codeing = utf-8 -*-
# @Time : 2021-06-16 0:15
# @Author : yjh
# @File : test01.py
# @Software : PyCharm

import sys , socket

# 判断端口是否开放
def open(ip,port):
    s = socket.socket()
    try:
        s.connect((ip,port))
        return True
    except:
        return False

# 默认扫描的函数
def scan(ip,portlist):
    for x in portlist:
        if open(ip,x):
            print("%s host %s port is open"%(ip,x))
        else:
            print("%s host %s port is close"%(ip,x))

# 范围扫描
def rscan(ip,s,e):
    e+=1 # range顾头不顾尾所以+1
    for x in range(s,e):
        if open(ip,x):
            print("%s host %s port is open"%(ip,x))
        else:
            print("%s host %s port is close"%(ip,x))

def main():
    defaultport = [135,139,445,1433,3306,3389,5944]

    if len(sys.argv)==2: # 如果只填了一个参数 ip
        if sys.argv[1][0]=="-":
            option = sys.argv[1][1:] # 看一下后面是什么如 -version ,-help
            if option=="version":
                print("当前版本号为1.0")
            elif option=="help":
                print("输入 : python xxx.py <ip> <port : 80,90,88...或80-100或不输入>")
            sys.exit()

        # 没有输入端口号
        scan(sys.argv[1],defaultport)

    # 如果加了端口号,分两种形式(80,90,.. / 80-100)
    if len(sys.argv)==3:
        # 有逗号的形式
        if "," in sys.argv[2]:
            p = sys.argv[2] # 字符串 80,90,100
            p = p.split(",") # ['80','90','100']
            a = []
            for x in p:
                a.append(int(x))
            scan(sys.argv[1],a)
            sys.exit()

        #  有-的形式
        if "-" in sys.argv[2]:
            p = sys.argv[2]
            p = p.split("-") # ['80','100']
            s = int(p[0])
            e = int(p[1])
            rscan(sys.argv[1],s,e)
            sys.exit()

if __name__ == '__main__':
    main()

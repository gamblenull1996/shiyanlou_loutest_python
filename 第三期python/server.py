# -*- coding:utf-8 -*-

"""
1. 添加服务器(add 命令)：支持以下参数-h hostip -u user -p password
三个参数必须填写，否则报错
实例：server.py add -h 127.0.0.1 -u shiyanlou -p shiyanlou
2. 列出服务器(list 命令) 没有参数 列出当前存储的所有服务器信息
实例: server.py list
$ server.py list
127.0.0.1 shiyanlou shiyanlou
192.168.1.1 ubuntu password
3. 删除服务器(delete) 支持参数-h hostip
实例：delete -h 127.0.0.1 成功的话无输出

服务器信息要求使用文件存储 存储位置
/home/shiyanlou/serverinfo

错误处理方式 返回一条ERROR启示错误信息
1.参数不足 server.py add -h 127.0.0.1 -u shiyanlou
2.命令不支持 server.py test
3.server.py add 已经添加过了 例如连续执行两次相同的add命令
4.server.py delete 如果服务器不存在也要报错 正常退出

"""
import os
import sys


def add(addlist):
    if len(addlist) == 6:
        hostip = addlist[1]
        user   = addlist[3]
        password = addlist[5]

        with open("./serverinfo/serverinfo.log", "a+") as f:
            line = f.readline()
            while line:
                flag = hostip in line
                if flag == True:
                    print "ERROR:record already existed"
                    return
                line = f.readline()
            f.write("%s %s %s \n "%(hostip, user, password))
    else:
        print "ERROR:lack of parameter number!"

def list():
    with open("./serverinfo/serverinfo.log", "r") as f:
        listlist  = f.read()
        print listlist

def delete(deletelist):
    if len(deletelist) == 1:
        ip = deletelist[0]
        with open("./serverinfo/serverinfo.log", "r") as f:
            line = f.readline()
            while line:
                flag = ip in line
                if flag == True:
                    with open("./serverinfo/out.log", "w") as out:
                        out.writelines([line for line in f.readlines() if ip not in line])
                    return True
                line = f.readline()
            print "ERROR:can't find ip in file"
            return False


    else:
        print "ERROR:no ip adderess provided"


if __name__ == '__main__':

    if sys.argv[1] == "add":
        add(sys.argv[2:])
    elif sys.argv[1] == "list":
        list()
    elif sys.argv[1] == "delete":
        flag = delete(sys.argv[2:])
        if flag == True:
            os.remove("./serverinfo/serverinfo.log")
            os.rename("./serverinfo/out.log", "./serverinfo/serverinfo.log")
    else:
        print "ERROR:not supported method. try add, list, delete"




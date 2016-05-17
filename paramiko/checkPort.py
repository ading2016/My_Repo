# -*- coding: utf8 -*-
__author__ = 'Administrator'
import MySQLdb
import socket
import time
import string
import thread
import re
socket.setdefaulttimeout(5)
global iplist1
iplist1 = []
def socket_port(ip, port):
    """
    输入IP和端口号，扫描判断端口是否开放
    """
    try:
        #if port>=65535:
        #    print u'端口扫描结束'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect_result = s.connect_ex((ip, port))
        #print connect_result
        if connect_result == 0:
            print ip, u':', port, u'端口开放'
            iplist1.append(ip)
            return 1
        s.close()
    except:
        #print u'端口扫描异常'
        pass
#socket_port("121.207.242.224", 443)
db = MySQLdb.connect(host="192.168.9.80", user="ading", passwd="ading", db="srv_table",port=3307)
cursor = db.cursor()
cursor.execute("set names utf8;")
count = cursor.execute("select  inter_ip ,local_ip from a_table  where admin='林天来'; ")
db1 = MySQLdb.connect(host="192.168.9.80", user="ading", passwd="ading", db="named",port=3307)
cursor1 = db1.cursor()
cursor1.execute("set names utf8;")
count1 = cursor1.execute("select top, rdata from rdata where domain='99.com' ;")
print count
result = cursor.fetchall()
result1 = cursor1.fetchall()
print list(result1)
'''
print list(result)
for ipa in list(result):
    for ipb in list(ipa):
        if ipb == "210.73.212.66":
            print ipb
'''
ipplist = []
for iplist in list(result):
    for wor in list(iplist):
        if wor is None:
            pass
        elif wor == "None":
            pass
        elif wor == "":
            pass
        elif "/" in wor:
            #print wor.split("/")[0]
            socket_port(wor.split("/")[0], 443)
            ipplist.append(wor.split("/")[0])
        elif "\\" in wor:
            #print wor.split("/")[0]
            socket_port(wor.split("\\")[0], 443)
            ipplist.append(wor.split("\\")[0])
        else:
            #print wor
            socket_port(wor, 443)
            ipplist.append(wor)

print iplist1
for ipa in iplist1:
    for domainlist1 in list(result1):
        if ipa in list(domainlist1):
            print list(domainlist1)





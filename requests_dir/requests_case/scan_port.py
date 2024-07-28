# -*- coding: utf-8 -*-
import socket
import nmap
from socket import *


def connScan(tgtHost, tgtPost):
    s = None
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((tgtHost, tgtPost))
        s.send('test\n')
        result = s.recv(100)
        print('[+] %d /tcp open' % tgtPost)

    except:
        print('[+] %d /tcp closed' % tgtPost)
    finally:
        if s:
            s.close()

def portScan(tgtHost, tgtPosts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        return

    try:
        tgtName = gethostbyaddr(tgtIp)
        print('[+] scan result name : ', tgtName)
    except:
        print('[+] scan result name ip : ', tgtIp)

    setdefaulttimeout(1)

    for tgtPost in tgtPosts:
        # print('scan port ', tgtPost)
        connScan(tgtHost, int(str(tgtPost).strip()))


if __name__ == '__main__':
    tgt_host = '192.168.88.61'
    tgt_ports = '21, 22, 443, 8080, 10012, 40012'
    tgt_port_list = tgt_ports.split(',')
    portScan(tgt_host, tgt_port_list)

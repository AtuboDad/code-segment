# -*- coding: utf-8 -*-
import nmap

nm = nmap.PortScanner()
nm.scan('192.168.88.61', '22-443')
command_line = nm.command_line()

scaninfo = nm.scaninfo()

hosts = nm.all_hosts()

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()

        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

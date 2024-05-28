# -*- coding: utf-8 -*-
import socket
from concurrent import futures

ip_list = []

def get_ip_status(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip, port))
        ip_list.append(port)
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip, port))
        pass
    finally:
        server.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    with futures.ThreadPoolExecutor(3000) as executor:
        for port in range(10000, 75000):
            # get_ip_status(host, port)
            executor.submit(get_ip_status, host, port)
    executor.shutdown()
    print(ip_list)

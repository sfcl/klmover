#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def check(addr):
    """
        Проверка доступности хоста по TCP порту. Принимает на ход 
        IP адрес, либо символическое имя компьютера.
    """
   
    """
    if addr.count('.') == 3:
        # случай для ip v4 адреса 
        ip_addr = addr
    elif addr.count(':') >= 2:
        # случай для ip v6 адреса
        ip_addr = addr
    else:
        # во всех остальных случаях, например символическое имя
        #print('gethostbyname=', addr)
        ip_addr = socket.gethostbyname(addr)
    """
    ip_addr = addr
    
    tcp_port = 135 # Client/Server Communication CIFS
    rez = None
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(15)
        s.connect((ip_addr, tcp_port))
    
    except OSError as msg:
        rez = None
        s.close()
        return rez
    
    rez = True
    return rez
    
if __name__ == '__main__':
    ip = '10.89.30.13'
    spam = check(ip)
    if spam :
        print('Подключение прошло успешно!')
    else:
        print('Облом...')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, freeze_support
import subprocess

from tcping import check
from config import config
from config import pcs

version = '0.1'

def move_computer(pc):
    # переподключение компьютера к новому Kaspersky Security Center
    kes= r'klmover.exe -address ' + config['IP_KSC']
    
    # cmd_exec справедливо для NetworkAgent 8
    cmd_exec = r'psexec \\'+ pc + r' -accepteula -w "C:\Program Files\Kaspersky Lab\NetworkAgent 8"' + ' cmd /c ' + kes 
    
    # cmd_exec для NetworkAgent 10
    #cmd_exec = r'psexec \\'+ pc + r' -accepteula -w "C:\Program Files\Kaspersky Lab\NetworkAgent"' + ' cmd /c ' + kes 
    
    # важно отсутствие завершающего слэша в пути опции - w
    # print(cmd_exec)
    subprocess.call(cmd_exec)
    
count_computers = len(pcs)

if __name__ == '__main__':
    freeze_support()
    print('Кол-во перемещаемых ПК: ', count_computers)
    procs = {}
    for i in pcs:
        if check(i):
            # если ПК доступен, значит создаём новый тред, иначе пропускаем
            procs[i] = Process(target= move_computer, args= (i, ) ) 
        else:
            print('Хост ', i, ' недоступен!')
            continue

    for i in procs:
        print('Запускаю процесс ', i)
        procs[i].start()

    for i in procs:
        procs[i].join()

    print('')
    print('Родитесльский процесс завершон')

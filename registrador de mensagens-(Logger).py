#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 11:337:50 2019

@author: pevifol
"""
import time as t
import os
def data():
    '''Retorna uma string com a data atual no formato dia_mês_ano'''
    a=list(t.localtime())
    return str(a[2])+'_'+str(a[1])+'_'+str(a[0])
def logging(mensagem=''):
    '''Faz/adiciona ao log diário alguma coisa.'''
    mensagem=' - '+str(mensagem)
    try:
        os.stat("log")        
    except OSError:
        print('Criando diretório de log')
        os.mkdir("log")
    with open("./log/"+data()+'.txt','a+') as w:
        w.write(t.strftime("%H:%M:%S", t.gmtime())+mensagem+'\n')
    return
logging(69)
logging('Nice')
#!/usr/bin/env python3
# encoding: utf-8
"""
OrderedDictionaries.py

Created by Marko on 2010-08-01.
Copyright (c) 2010 Bstards. All rights reserved.
"""

"""=========================================
Nuevas caracteristicas en Python3.1
	Diccionarios Ordenados
	collections.OrderedDict
========================================="""

#import collections.OrderedDict

dic = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

print ('Diccionario original: ', dic)

#dicOrdenado = collections.OrderedDict( dic )
dicOrdenado = OrderedDict( sorted(dic.items(), key=lambda t: t[0]) )
#print (dicOrdenado)
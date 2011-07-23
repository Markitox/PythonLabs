#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
Lists.py

Created by Marko on 2010-02-25.
Copyright (c) 2010 Bstarts. All rights reserved.
"""

unaLista = [1,3,5,6]

print unaLista

print "Elemento con el indice 2:", unaLista[2]

print "Elemento con el indice -2:", unaLista[-2]

unaLista[0:0] = [9,7,8]

print "Agregamos elementos: ", unaLista

unaLista[1:3] = []

print "Eliminamos elementos:", unaLista
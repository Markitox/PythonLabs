#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
IfControlFlow.py

Created by Marko on 2010-02-25.
Copyright (c) 2010 Bstards. All rights reserved.
"""

num = int( raw_input("Ingrese un numero: ") )

if num == 0:
	print "digito cero"
elif num < 0:
	print "digito negativo"
elif num > 0:
	print "digito positivo"
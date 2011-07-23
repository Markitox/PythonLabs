#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
ForControlFlow.py

Created by Marko on 2010-02-27.
Copyright (c) 2010 Bstards. All rights reserved.
"""

otraLista = range(7)

print "Lista de digitos: ", otraLista

otraLista = range(20,0,-1)

print "Lista de digitos: ", otraLista

otraLista = range(2,30,2)

print "Lista de digitos: ", otraLista

listaVacia = [None]*5

print "Lista vacia: ", listaVacia
	
unaLista = ["MontePokara","Pinotepa","uno"]

for s in unaLista:
	print "Elemento: " + s + " de longitud:", len(s)

	
print "\nModificamos la lista mientras se itera"
contador = 0
strAux = ""

for s in unaLista:
#	print unaLista
	print "Elemento: " + s + " de longitud:", len(s)
	
	if strAux != s:
		contador = 0
	
	contador += 1
	if len(s) > 7 and contador < 10:
		unaLista.insert(0, s.rjust( contador + len(s) ))
	
	strAux = s

print unaLista
#!/usr/bin/env python
# encoding: utf-8
"""
ProgramacionFuncional.py

Created by Marko on 2010-05-09.
Copyright (c) 2010 Bstards. All rights reserved.
"""

"""
	Lenguaje Funcional: La programacion funcional es un paradigma en el que la programacion 
	se basa casi en su totalidad en funciones, entendiendo el concepto de funcion segun su 
	definicion matematica, y no como los simples subprogramas de los lenguajes imperativos 
	que hemos visto hasta ahora.
	
	En los lenguajes funcionales puros un programa consiste exclusivamente en la aplicacion 
	de distintas funciones a un valor de entrada para obtener un valor de salida
	
	El objetivo es conseguir lenguajes expresivos y matemáticamente elegantes, en los que no sea 
	necesario bajar al nivel de la máquina para describir el proceso llevado a cabo por el programa.
	
	Aun que Python no es un lenguaje puramente Funcional, contiene varias caracteristicas de 
	un lenguaje Funcional
"""

#	Funciones de orden Superior

def unaFuncion():
	print 'Hola Mundo'
	
unaReferenciaFuncion = unaFuncion

unaReferenciaFuncion()


listaNumeros = [6,8,3,5,9]

print listaNumeros
listaNumeros.sort()
print listaNumeros

def fun(x, y):
	return 1 if ( x < y ) else ( -1 if (x > y) else 0 )

	
listaNumeros.sort( fun )

print listaNumeros


#	Funciones de orde superior en iteraciones, MAP, FILTER, REDUCE

def cuadrado(x):
	return x ** 2

listaCuadrados = map(cuadrado, listaNumeros)

print listaCuadrados

# Funciones Lambda, funciones anonimas; estan restringidas por ser, por sintaxis,
#	una sola expresion.

listaCuadrados.sort(lambda x, y: -1 if (x < y) else (	1 if ( x > y ) else 0) )

print listaCuadrados
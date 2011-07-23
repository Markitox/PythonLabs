#!/usr/bin/env python
# encoding: utf-8
"""
Functions.py

Created by Marko on 2010-02-27.
Copyright (c) 2010 Bstards. All rights reserved.
"""

# La sentencia continua de la definicion de la funcion es la cadena de Documentacion #docstring
# http://docs.python.org/tutorial/controlflow.html#tut-docstrings
def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print a, ", ",
		a, b = b, a+b
	

fib(10)

# Definicion de funcion con argumentos con valor por default

def fib2( n=0 ):
	a, b = 0, 1
	result = [a]
	
	while a < n:
		if a:
			result.append( a )
			
		a, b = b, a+b
	
	return result

print
print fib2()
print fib2(10)


def unaFuncion( parametroRequerido, opcional1=1, opcional2=2, opcional3="-", opcional4=None ):
	print "[parametroRequerido: ", parametroRequerido, ", ",
	print "opcional1: ", opcional1, ", ",
	print "opcional2: ", opcional2, ", ",
	print "opcional3: ", opcional3, ", ",
	print "opcional4: ", opcional4, "]"
	
unaFuncion( 90 )
unaFuncion( 80, "a" )
unaFuncion( 70, 10 )
unaFuncion( 60, 10, 20 )
unaFuncion( 50, 10, 'oO0Oo', 30 )
unaFuncion( 40, 10, 20, 30, 50 )

# Es posible pasar los valores con el formato llave:valor, como un diccionario, mapa
unaFuncion(70, opcional3='GgG')


"""
	Es posible recibir una lista de parametros o un dicionario de parametros 
"""

def funcionCompleja( unParametro, *lista, **diccionario ):
	print "Parametro simple: ", unParametro, ', ',
	print "lista Parametros: ", lista, ', ',
	print "diccionario: ", diccionario
	
funcionCompleja('sdf', 'Kolopolo', 2, 3, "Ultimo", valor1="12", valor2="o00o")
funcionCompleja(234, 'Koleoptero', 2, 3, "Ultimo", valor1="12", valor2=00)


"""
	Es posible pasar una lista pero se especifica que debe ser desempacada con el operador *,
	distribuyendo los valores de la lista sobre los parametros
"""

def desempacaParametros( unParametro, *lista ):
	print "Parametro simple: ", unParametro, ", ",
	print "Lista: ", lista

unaLista = ['yepa', 'yepa', 33]

desempacaParametros( unaLista )
#	Usando el operador
desempacaParametros( *unaLista )


#	Decoradores

print '===================[ Decoradores ]====================='

def decorador( funcion ):
	
	def nuevaFuncion( *args ):
		print 'Llamada a la funcion: ', funcion.__name__
		retorno = funcion(*args)
		return retorno
	return nuevaFuncion
	
def saludo( mensaje ):
	print mensaje
	
saludo('Hola Mundo')

f = decorador( saludo )

f('Hola Mundo')

#	Al anteponer @ y el nombre del decorador a la funcion que queremos decorar, 
#	todas las invocaciones estaran decoradas

@decorador
def saludo2( mensaje ):
	print mensaje
	
saludo2( 'Hola mas Mundo' )
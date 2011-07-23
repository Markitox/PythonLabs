#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

"""
HelloWorld.py

Created by Marko on 2010-02-21.
Copyright (c) 2010 Bstards. All rights reserved.
"""
#	Comentario en Python

print 'Hola Mundo'

# con '\' al final de la linea dentro de una cadena se especifica que continua la cadena en la siguiente linea
print "Saludos!!\
\n	\
	Continuacion de la cadena\n\
"

# Otra forma es usar triple ' o "
print """	Hola
Esto es una cadena compleja', "saber"
"""

#	Una cadena cruda, se antepone el caracter 'r' a la cadena
print r"Una cadena que contiene \n\
y algo mas\
"

#	Operadores sobre cadenas
print "===========[ Operadores sobre cadenas '+', '*' ]============\n"

unaCadena = 'Firma congruencial'
otraCadena = unaCadena + ', Facilidades operacionales'

print otraCadena
print unaCadena*3
print 4*unaCadena
#	la siguiente forma de concatenacion solo funciona con cadenas explicitas, 
#	no con variables o expresiones de cadenas
print 'unaCadena'  'otraCadena'

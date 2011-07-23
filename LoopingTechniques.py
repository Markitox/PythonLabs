#!/usr/bin/env python
# encoding: utf-8
"""
LoopingTechniques.py

Created by Marko on 2010-03-14.
Copyright (c) 2010 Bstards. All rights reserved.
"""

#	Iterando dicionarios

mapaPaises = {'Mexico':"Ciudad de Mexico", 'Canada':"Ottawa", 'Francia':"Paris", 'Suiza':"Berna"}

for key, value in mapaPaises.iteritems():
	print "Pais: ", key, ", su capital es: ", value

print 'Llaves: ', mapaPaises.keys()
print 'Valores: ', mapaPaises.values()

#	Iterando una lista

print "====[Iterando la lista con indices]===="

listaRios = ['Panuco', 'Lerma', 'Usumacinta', 'Grijalva']

for index, value in enumerate( listaRios ):
	print "Rio ", index, ": ", value

for index in range( len(listaRios) ):
	print "Rio[", index, "]: ", listaRios[index]


"""
#	
#	La funcion 'zip' devuelve una tupla de las listas que se le pasen, 

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print zipped

x2, y2 = zip(*zipped)

print x2, ", " , list( x2 )
print y2, ", " , list( y2 )
"""

#	Una forma de iterar varias listas se usa la funcion zip

listaPaises = mapaPaises.keys()
listaCiudades = mapaPaises.values()

tuplaPaisCiudad = zip(listaPaises, listaCiudades )

#	Tupla Pais con ciudad
print tuplaPaisCiudad

for pais, ciudad in tuplaPaisCiudad:
	print 'La ciudad de {0} es: {1}.'.format(pais, ciudad)
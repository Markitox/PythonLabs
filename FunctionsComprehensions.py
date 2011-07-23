#!/usr/bin/env python
# encoding: utf-8
"""
FunctionsComprehensions.py

Created by Marko on 2010-03-13.
Copyright (c) 2010 Bstards. All rights reserved.
"""

#	Las listas comprensibles, hacen uso de las sentencias FOR, IF por lo menos, para generar 
#	una lista con ciertas caracteristicas u orden
#	Son mas flexibles, y permiten expresiones complejas en una linea

listaFrutas = ['uva', 'fresa', 'kiwi', 'mandarina']

print 'Lista de frutas: ', [ fruta.capitalize() for fruta in listaFrutas ]

listaNumeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print 'Lista numeros: ', [dig*dig for dig in listaNumeros]

print 'Lista numeros impares: ', [dig**2 for dig in listaNumeros if dig % 2]

print 'Lista numeros pares: ', [ (dig, dig**2) for dig in listaNumeros if not (dig % 2)]

#	Multiples sentencias FOR

lista1 = [1,2,3]
lista2 = [10,20,30]

print "Multiples FOR: ", [ i+j for i in lista1 for j in lista2 ]

print "Multiples FOR: ", [ lista1[i] + lista2[i] for i in range( len(lista2) ) ]


#	Ejemplos sobre listas internas

matriz = [
		[1,2,3],
		[4,5,6],
		[7,8,9]
	]

print "matriz: ", [ [fila[index]*5 for fila in matriz] for index in range( len(matriz[0]) ) ]

print "Original {matriz}"
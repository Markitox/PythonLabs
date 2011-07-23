#!/usr/bin/env python3
# encoding: utf-8

"""
	Demostracion de creacion de Clases en Python
	
	NOTA: Python no soporta sobrecarga de metodos, lo que hace es mantener la ultima implementacion del
	metodo que encuentre. Para poder soportar este comportamiento es declarar sobre el metodo un 
	argumento de tipo tupla
	
	def metodo (self, *unaTuplaDeArgumentos)
	
"""

class Persona:
	"""
		Clase Persona
		Identifica a un objeto de la vida real
	"""
	
#	def __init__(self):
#		print 'Instancia default del objeto Persona'
		
	def __init__(self, *params):
		print ('Instancia con parametros:', params, ' de la clase Persona')
		
		
persona = Persona()
persona = Persona('Marko')
persona = Persona(23, 6)
persona = Persona('Kiko', 9)

"""
	Para que una variable de clase pueda ser private se debe de poner el prefijo '__', Aunque 
	lo unico que hace Python es reenombrar esa variable a un formato que conoce
"""

import datetime

class Coche(object):
	
	def __init__(self):
		self.__modelo = datetime.date.today().year
	
	def getModelo(self):
		print ('~invocando el metofo GET, ',)
		return self.__modelo
		
	modelo = property(getModelo)
	
coche = Coche()

print ('1. Modelo del coche: ', coche.modelo )
print ('2. Modelo del coche: ', coche.getModelo() )
print ('3. Modelo del coche: ', coche._Coche__modelo )


"""
	Python tiene una caracteristica que permite definir metodos set/get para propiedades 
	de la clase, pero usa el nombre de la propiedad y tras bambalinas usa los metodos definidos
	
"""

class OtraPersona(object):
	
	def __init__(self):
		self.__nombre = '.'
	
	def getNombre(self):
		print ('\n[OtraPersona] regresando el nombre\n' )
		return self.__nombre
		
	def setNombre(self, nombre):
		print ('\n[OtraPersona] asignando nombre\n' )
		self.__nombre = nombre

	nombre = property(getNombre, setNombre)

otraPersona = OtraPersona()

otraPersona.setNombre('Flaca')

print ('Nombre de OtraPersona: ', otraPersona.nombre )

otraPersona.nombre = 'Marko'
#otraPersona.setNombre('Marko')

print ('Nombre modificado de OtraPersona: ', otraPersona.getNombre() )
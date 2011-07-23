#!/usr/bin/env python
# encoding: utf-8
"""
DescriptorAndProperties.py

Created by Marko on 2010-06-27.
Copyright (c) 2010 Bstards. All rights reserved.
"""

"""
	El Descriptor Protocol se compone de 3 metodos:
		__get__
		__set__
		__delete__
	
	El descriptor es el atributo que sera asociado
"""

class MiDescriptor(object):
	
	def __get__(self, instance, owner):
		
		if ( not hasattr(self, '_value') ):
			raise AttributeError
		
		print 'Obteniendo valor: %s' % self._value
		
		return self._value


	def __set__(self, instance, value):
		print 'Asignando valor %s' % value
		self._value = value
			

class MiClase(object):
	
	miDescriptor = MiDescriptor()


miClase = MiClase()

miClase.miDescriptor = 23
print miClase.miDescriptor
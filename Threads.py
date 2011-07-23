#!/usr/bin/env python
# encoding: utf-8
"""
Threads.py

Created by Marko on 2010-05-23.
Copyright (c) 2010 Bstards. All rights reserved.
"""

"""
	Los hilos en Python son controlados por Global Interpreter Lock GIL, 
	este modulo solo permite la ejecucion de un solo Thread, lo que posibilita
	la facilidad de creacion de extensiones en C pero tiene gran desventaja 
	en el rendimiento de la app, por lo cual es muy cuestionado el uso de 
	Threads y mejor se haga uso de procesos.
	
	Otra opcion es usar Jython o IronPython ya que estos no tienen el GIL
"""

import threading

class MiThread( threading.Thread ):
	
	def __init__( self, num ):
		threading.Thread.__init__(self)
		self.num = num

	def run( self ):
		print "Soy el hilo: ", self.num, ", name: ", self.name
#		print "threading.activeCount: ", threading.activeCount


print "Hilo principal======================\n"

for i in range(0, 10):
	t = MiThread( i )
	t.start()
	t.join()

print "\n++++++++++++++++Sincronizacion++++++++++++++++"

def syncronized( lock ):
	
	def dec( f ):
		
		def funcDec(*args, **kwargs):
			lock.acquire()
			try:
				return f(*args, **kwargs)
			finally:
				lock.release()
		return funcDec
	return dec

class MyThreadDecorated( threading.Thread ):
	
	@syncronized(threading.Lock())
	def run(self):
		print "Metodo Sicronizado...."

t = MyThreadDecorated()
t.start()
t.join()
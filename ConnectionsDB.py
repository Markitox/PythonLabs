#!/usr/bin/env python
# encoding: utf-8
"""
ConnectionsDB.py

Created by Marko on 2010-05-24.
Copyright (c) 2010 Bstards. All rights reserved.
"""

import sqlite3 as dbapi

connection = dbapi.connect("SQLite.bd")

print connection

cursor = connection.cursor()

#cursor.execute("""create table empleados (dni text, nombre text, departamento text)""")

#cursor.execute("""insert into empleados values (?, ?, ?)""",
#		('456', 'Marko', 'Sistemas') )
#connection.commit()


cursor.execute("""select * from empleados""" )

for registro in cursor.fetchall():
	print registro

cursor.close()
connection.close()

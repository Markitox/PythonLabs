#!/usr/bin/env python
# encoding: utf-8
"""
Test.py

Created by Marko on 2010-05-28.
Copyright (c) 2010 Bstards. All rights reserved.
"""

import sys
import os
import unittest
from unittest import TestCase

class Test:
	def __init__(self):
		pass


class TestTests(unittest.TestCase):
	def setUp(self):
		pass
	
	def testInstance(self):
		"""docstring for testInstance():"""
		
		self.assertEqual(1,1,msg='No Son Iguales')
#		pass
	


if __name__ == '__main__':
	unittest.main()
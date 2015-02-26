#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
"""
try:
	f=open('README.md', 'r')
	f.read()
finally:
	f.close()
"""

with open('README.md', 'r') as f:
	print f.read()
	for line in f.readlines():
		print(line.strip())
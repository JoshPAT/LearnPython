#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

#print current directory&files
import os
print [d.lower() for d in os.listdir('.')]
print os.listdir('.')

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s, str) == True else s for s in L]

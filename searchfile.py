#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

import os

def search(s):

	return '\n'.join([os.path.join(root, i) for root, dirs,files in os.walk('.') for i in files if s in i])

print search('00')   
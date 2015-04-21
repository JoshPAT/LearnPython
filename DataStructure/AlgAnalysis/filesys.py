#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh zhou'

import os

def disk_usage(path):
	total = os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			childpath = os.path.join(path, filename)
			total += disk_usage(childpath)
	print ('{0:<7}'.format(total), path)
	return total

disk_usage('/Users/JoshPAT/Documents/learngit/LearnPython/DataStructure
	')
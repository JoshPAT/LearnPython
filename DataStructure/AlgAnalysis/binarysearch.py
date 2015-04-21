#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh zhou'

def binary_search(data, target, low, high):
	if target <= data[0]:
		return data[0] == target
	if low > high:
		return False
	else:
		mid = (high + low) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search(data, target, low, mid+1)
		else:
			return binary_search(data, target, mid+1, high)

L = [2,4,5,6,7,8,14,17,19,22,25,29,33,37,27,99]


print sorted(L)
print len(L)
print binary_search(sorted(L), 1, 0, 14)

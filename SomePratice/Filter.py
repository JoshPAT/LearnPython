#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
请尝试用filter()删除1~100的素数;以及前100个素数求和。
"""
import math
def is_prime(x):
	if x == 1:
		return False 
	if x == 2:
		return True
	for i in range(2,int(math.sqrt(x))+1):
		if x%i == 0:
			return False
	return True

print filter(is_prime,range(1,101))
print reduce(lambda x,y: x+y ,filter(is_prime,range(1,101)))
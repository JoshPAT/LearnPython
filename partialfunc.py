#!/usr/bin/env python
# -*- coding: utf-8 -*-
#当函数的参数个数太多，
#需要简化时，使用functools.partial可以创建一个新的函数，
#这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

import functools
max2 = functools.partial(max,55 )
print max2(5,4,2)

def origin(int,int1,*args,**kw):
	print int,int1
	print args
	print kw

origin(1,2,2,3,usr="pwd")

simplefunc = functools.partial(origin,1,2,3,3, admin ="goodpwd")

simplefunc()


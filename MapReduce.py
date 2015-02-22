#!/usr/bin/env python
# -*- coding: utf-8 -*

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def sTr2Str(x):
	#return x[0].upper()+x[1:].lower()
	return x.capitalize()

print map(sTr2Str,['adam', 'LISA', 'barT'])

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(l):
	return reduce(lambda x,y :x*y , l)
print prod([1,2,3,4])

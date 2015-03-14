#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In python, this is used to define variable parameters
# "*"here means tuple is used
# "**"here means dictionary is used

def info1(name, age , **other):
	print 'name:', name ,'age:' ,age ,'other:',other 

def info2(name, age , *other):
	print 'name:', name ,'age:' ,age ,'other:',other

def info3(name, age, *tuple, **dic):
	print 'name:', name ,'age:' ,age ,'tuple:',tuple ,'dic:', dic

info1("我是不一样的烟火",24,wo = "wo11" , shi = "我me")
info2("我是不一样的烟火",24,"我","就","是","我")

args = (1, 2, 3, 4)
kw = {'x': 99}
info3(*args, **kw)

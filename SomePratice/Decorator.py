#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

"""
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
	print "2015-2-22"

now()
print now.__name__

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s ():' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log('begin')
def now():
	print "2015-2-22"
now()
"""

def log(func):
	def wrapper(*args,**kw):
		print "begin call:%s"%func.__name__
		func(*args,**kw)
		print "end call:%s"%func.__name__
	return wrapper

@log
def now(x,y):
	print "2015-2-22"
	print x+y
now(1,2)
print "\n"


import functools
 
def log(arg):
    if hasattr(arg, '__call__'): #判断 "arg'是不是一个被call的方法。
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print 'begin call : %s()' % arg.__name__
            arg(*args, **kw)
            print 'end call'
        return wrapper
        
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s()' % (arg, func.__name__)
            func(*args, **kw)
            print 'end call'
        return wrapper
    return decorate
    
@log('excute')
def now():
    print '2015-2-22'
    
now()
 
@log
def now():
    print '2015-2-22'
    
now()




#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
#bound the attribute by __slot___
class Me(object):
	__slots__ = ("arg","brg")
	"""docstring for Me"""
	def __init__(self,arg,brg ):
		self.arg = arg
		self.brg = brg

me = Me(1,2)
print me.arg 
#no bound case
class Metoo(object):
	"""docstring for Me"""
	def __init__(self,arg,brg ):
		self.arg = arg
		self.brg = brg

me = Metoo(1,2)
me.abc = 3
print me.abc
#Use set_score to confine the range of score
#Use get_score to decide whether there is a score
class Student(object):
    
    @property
    def score(self):
        if hasattr(self,"_score"):
        	return self._score
        else:
        	raise ValueError('no score now')

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


abc = Student()

abc.score =99
print abc.score

# use property to do simple coding
class Student(object):

    @property
    def birth(self):
        if hasattr(self,"_birth"):
        	return self._birth
        else:
        	return 2014 - self._age

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        if hasattr(self,"_birth"):
        	return 2014 - self._birth
        else:
        	return self._age

    @age.setter
    def age(self,value):
    	self._age = value

ccc,bbb = Student(),Student()
ccc.age  = 24

print ccc.bi rth 
print ccc.age 

bbb.birth = 1990

print bbb.birth
print bbb.age


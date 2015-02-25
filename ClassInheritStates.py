#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print "Animal is running"
	def eat(self):
		print "It is eating now"
class Dog(Animal):
	def run(self):
		print "Dog is running"
class Cat(Animal):
	def run(self):
		print "Cat is running"

dog = Dog()
cat = Cat()

def run_twice(object):
	object.run()
	object.run()

run_twice(cat)

cat.eat()
print type(cat)

print dir(cat)
print cat.__class__

print dir
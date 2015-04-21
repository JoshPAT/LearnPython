#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh zhou'

class Progression(object):

	def __init__(self, start=0):
		self._current = start

	def _advance(self):
		self._current += 1

	def __next__(self):
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		''' By convention, an iterator must return itself as an iterator'''
		return self

	def print_progression(self, n):
		print (' '.join(str(self.__next__()) for j in range(n)))

test = Progression()
test.print_progression(9)

class ArithmeticProgession(Progression):

	def __init__(self, increment=1, start=0):

		super(ArithmeticProgession, self).__init__(start)
		self._increment = increment

	def _advance(self):
		self._current += self._increment

test = ArithmeticProgession(4)
test.print_progression(9)

class GeometricProgession(Progression):

	def __init__(self, increment=1, start=1):

		super(GeometricProgession, self).__init__(start)
		self._increment = increment

	def _advance(self):
		self._current *= self._increment

test = GeometricProgession(4)
test.print_progression(9)


class FibonacciProgression(Progression):

	def __init__(self, first=0, second=1):
		super(FibonacciProgression, self).__init__(first)
		self._current = first
		self._next = second

	def _advance(self):
		self._current, self._next =  self._next, self._current + self._next

test = FibonacciProgression(0,1)
test.print_progression(9)








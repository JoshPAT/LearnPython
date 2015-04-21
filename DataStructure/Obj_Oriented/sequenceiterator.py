#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh zhou'

class SequenceIterator:
	'''An iterator for any of Python's sequence types'''

	def __init__(self, sequence):
		self._seq = sequence
		self._k = -1

	def __next__(self):
		self._k += 1
		if self._k < len(self._seq):
			return self._seq[self._k]
		else:
			raise StopIteration()
	def __iter__(self):
		return self

cc = SequenceIterator([1,2,3])

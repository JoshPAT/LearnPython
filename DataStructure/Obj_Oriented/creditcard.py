#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
A Simple Class object in good coding style.
'''

__author__ = "Josh zhou"

class CreditCard(object):
	def __init__(self, customer, bank, acnt, limit):
		self._customer = customer
		self._bank = bank
		self._acnt = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		return self._customer

	def get_bank(self):
		return self._bank

	def get_acnt(self):
		return self._acnt

	def get_limit(self):
		return self._limit

	def get_balance(self):
		return self._balance

	def charge(self, price):
		if self._balance + price > self._limit:
			return False
		else:
			self._balance += price
			return True

	def make_payment(self, amount):
		self._balance -= amount

cc = CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 1000)
print cc.get_limit()
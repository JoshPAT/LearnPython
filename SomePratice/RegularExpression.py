#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
"""
正则表达式是一种用来匹配字符串的强有力的武器。
它的设计思想是用一种描述性的语言来给字符串定义一个规则，
凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

Standard
# 1.\d用于匹配数字 , 2.\w匹配字母or数字 3.\s匹配空格 4. "."匹配任何字符 5.\-\ 匹配转义后的-
# \d\d\d -> 010 , \w\w\d -> aa0 or 010 , py. -> pyc or py3 or py@
#6.用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

examples：
#\d{3}\s+\d{3,8} -> 123  3333
#\d{3}\-\d{3,8} -> 111-33333

Advance
#[a-zA-Z\_][a-zA-Z\_]*[a-zA-Z\_]+[0-9a-zA-Z\_]{0, 19}
#7.^表示行的开头，^\d表示必须以数字开头。
#8.$表示行的结束，\d$表示必须以数字结束。

"""
import re
print 'as\\-a'
print r'as\\-a'
#test = raw_input('>^\d{3}\-\d{3,8}$')
test = '021-6222222'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print 'ok'
else:
    print 'failed'

#Split
print re.split(r'[\s\,\;]+', 'a,b;; c  d')
t= '1:1:51'
m =re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.group()

#Greedy Match
print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '102300').groups() #+? degreedy

#Pre-Compile the Regular Expression
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
if re.match(re_telephone, test):
    print 'ok'
else:
    print 'failed'
re_telephone = re.compile(r'^(<?[0-9a-zA-Z\_\.\ ]*>?)([0-9a-zA-Z\_\.]+)@(\w+).([a-zA-Z]+)$')
if re.match(re_telephone, '<josh zhou>joshzhou16@gmail.com'):
    print 'ok'
else:
    print 'failed'

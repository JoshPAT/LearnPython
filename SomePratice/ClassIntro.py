#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
# define a class
class Student(object):

    def __init__(self, name, score, x =0 , y =0):
        self.name = name
        self.score = score
        self.x =x
        self.y =y

    def print_score(self):
        print '%s: %s location:%d,%d' % (self.name, self.score,self.x ,self.y)

    def whereru(self):
    	print "I'm in %d %d " %(self.x ,self.y)

    def get_grade(self):
        if self.score == 1.0:
            return 'A'
        elif self.score <= 2.0:
            return 'B'
        else:
            return 'C'


zhouquan = Student("zhouquan", 1.0)
zhouquan.print_score()
zhouquan.whereru()
print zhouquan.get_grade()
zhouquan.age =8
print zhouquan.age
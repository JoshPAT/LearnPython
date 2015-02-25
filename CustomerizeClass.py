#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
"""
__str__ , __repr__
"""

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__

print Student("zhangsan")
zhangsan = Student("zhangsan")
print zhangsan

"""
__iter__
"""
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

for i in Fib():
	print i

class fib(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
a =fib()

print a[4]

"""
__getattr__
这种完全动态调用的特性有什么实际作用呢？
作用就是，可以针对完全动态的情况作调用
"""
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
a =Student()
print a.score

class Chain(object):

    def __init__(self, path=''):
        self._path = path + "s"

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.usr.timer
# Chain().status = Chain() + Chain("/status")
# when 
print Chain().status
print Chain() 
print Chain("/status")

"""
__call__
"""
class Student1(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)

 
abc = Student1('xiaoming')
abc()

print callable(Student1("status"))

#DynamicClass Build with type()
"""
要创建一个class对象，type()函数依次传入3个参数：
1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""
def fn(self, name='world'): # 先定义函数
	print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello = fn))

h =Hello()
h.hello()


#Meta Class
"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
"""


# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['ass'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

L = MyList()
print type(MyList)
print type(L)

"""
ORM全称“Object Relational Mapping”，即对象-关系映射。
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。
"""

print 2**38

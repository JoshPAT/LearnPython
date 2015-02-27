#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

"""
thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
"""
import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
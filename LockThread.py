#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-
import time, threading
#t1和t2是交替运行的
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        #获得lock
        lock.acquire()
        try:
        	change_it(n)
        finally:
        	#释放lock
        	lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#!/usr/bin/env python 2.7.8
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

print "Process (%s)start.." % os.getpid()

pid = os.fork()

if pid == 0:
	print "I am child Process %s , My Parent is Process %s" % (os.getpid(),os.getppid())
else:
	print "I created a child Process %s , My Process is %s" % (pid, os.getpid())

# Cool! Return twice!

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
	print 'Parent process %s' % os.getpid()
	p = Process(target = run_proc , args = ('test',))
	print 'Process will start'
	p.start()
	p.join()
	print 'Process end'
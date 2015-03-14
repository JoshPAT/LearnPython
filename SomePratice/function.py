#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def mov(x, y, step, angle):
	

	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

print mov(100,100,60,math.pi/6)

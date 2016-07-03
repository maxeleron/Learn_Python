#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Creating empty list
x = []
print x

# Generating list using *
x1 = [0] * 4
print x1

# Some list`s methods
xs = [ 0, 1, 2, 3, 4 ]
print xs

print len(xs)

print x[0]

x[0] = -1
print x[0]

xs.append(42)
print xs

del xs[0] # or xs.pop(0)
print xs

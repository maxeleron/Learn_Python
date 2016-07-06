# !/usr/bin/env python
#  -*- coding: utf-8 -*-

setExample = set()

xs = {1, 2, 3, 4}

print (42 in xs)

print (42 not in xs)

xs.add(42) # {1, 2, 3, 4, 42}
print xs

xs.discard(42) # {1, 2, 3, 4}
print xs

ys = {4, 5}

xs.intersection(ys)
print ( xs & ys )

xs.union(ys)
print ( xs | ys )

xs.difference(ys)
print ( xs - ys )
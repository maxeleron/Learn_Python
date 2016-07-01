# #!/usr/bin/env python
#  -*- coding: utf-8 -*-

import math

print u"Hello, user!!!\n"
print u"This is Calc\n"

a = input( u"Enter a: " )
b = input( u"Enter b: ")
c = input( u"Enter c: ")

D = b*b - 4*a*c

if D < 0:
    print u"No solution"
elif D == 0:
    x = (-b + math.sqrt(D)) / (2 * a)
    print u"x: ", x
else :
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print u"x1: ", x1
    print u"x2: ", x2

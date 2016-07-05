# #!/usr/bin/env python
#  -*- coding: utf-8 -*-

import math


def sqeq( a, b, c ):
    D = b * b - 4 * a * c
    if D < 0:
        print u"No solution"
    elif D == 0:
        x = (-b + math.sqrt(D)) / (2 * a)
        print u"x: ", x
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print u"x1: ", x1
        print u"x2: ", x2

print u"Hello, user!!!\n"
print u"This is awesome Calc\n"
print u"Please choose the act:\n 1 if +;\n 2 if -;\n 3 if *;\n 4 if /."

e0 = input( u"Enter a: " )
e1 = input( u"Enter b: ")
e2 = input( u"Enter c: ")

sqeq(e0, e1, e2)
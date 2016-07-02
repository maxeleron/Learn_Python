# #!/usr/bin/env python
#  -*- coding: utf-8 -*-

# Python 2.x has two types of strings.

# Byte string
str1 = b"Meat"

# Unicode string
str2 = u"Fish"

# You can use " or ' literals to create strings.
l1 = u"Wish"
l2 = u'Arial'

# Strings decoding.
newStr1 = str1.decode("utf-8")

# We can create new string like this.
s = "." * 10
print s

# Strings concatenation.
newS = "<" + s + ">"
print newS

# We can work with a letter (of string) using index
print l1[1]

# And one cool string method
before = "   foo bar     "
print before

after = before.strip()
print after
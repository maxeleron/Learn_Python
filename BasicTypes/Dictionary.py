# !/usr/bin/env python
#  -*- coding: utf-8 -*-

exampleDict = {} # or dict()

date = {"year": 2015, "month": "September"}

print len(date)

print date["year"]

print date.get("day", 7)

date["year"] = 2016
print date

del date["year"] # or date.pop("year")
print date

date = {"year": 2015, "month": "September"}

print date.keys()

print date.values()

print date.items()


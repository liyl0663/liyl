#!/usr/local/lib/python3.6
# -*- coding: UTF-8 -*-

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print('%s%s%s' % (i,j,k))
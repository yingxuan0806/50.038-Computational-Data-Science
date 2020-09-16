#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:55:57 2020

@author: yingxuan
"""

import sys

number_sales = 0
total_sales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    number_sales += 1
    total_sales += float(thisSale)
    
print(number_sales, "\t", total_sales)
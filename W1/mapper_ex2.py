#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:26:53 2020

@author: yingxuan
"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) == 6:
        data, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)
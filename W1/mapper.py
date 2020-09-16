#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:10:43 2020

@author: yingxuan
"""

#!/usr/bin/env python

import sys

for line in sys.stdin:
    data  = line.strip().split("\t")
    
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
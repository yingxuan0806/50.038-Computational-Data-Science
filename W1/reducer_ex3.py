#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:30:54 2020

@author: yingxuan
"""

import sys

existing_item = None
highest_sale = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    if len(data_mapped) != 2:
        continue
    
    current_item, current_sale = data_mapped
    
    if existing_item != current_item:
        
        if existing_item:
            print existing_item, "\t", highest_sale
            
        highest_sale = 0
    
    existing_item = current_item
    
    if float(current_sale) > float(highest_sale):
        highest_sale = current_sale
        
if existing_item is not None:
    print existing_item, "\t", highest_sale
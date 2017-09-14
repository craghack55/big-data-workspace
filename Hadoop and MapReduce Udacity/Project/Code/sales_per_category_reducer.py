#!/usr/bin/python

import sys

oldKey = None
totalSales = 0.0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    category, sales = data
    sales = float(sales)
    
    if oldKey is not None and oldKey != category:
        print(oldKey + "\t" + str(totalSales))
        totalSales = 0.0
        
    totalSales += sales
    oldKey = category
    
if oldKey is not None:
    print(category + "\t" + str(totalSales))
#!/usr/bin/python

import sys

oldKey = None
totalSales = 0.0
totalCount = 0.0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    sale, count = data
    count = int(count)
    sale = float(sale)
    totalSales += sale
    totalCount += count
    
    
print(str(totalSales) + "\t" + str(totalCount))
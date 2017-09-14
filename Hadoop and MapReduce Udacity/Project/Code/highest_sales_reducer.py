#!/usr/bin/python

import sys

oldKey = None
highestSale = 0.0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    store, sale = data
    sale = float(sale)
    
    if oldKey is not None and oldKey != store:
        print(oldKey + "\t" + str(highestSale))
        highestSale = 0.0
        
    
    if sale > highestSale:
        highestSale = sale
    
    oldKey = store
    
if oldKey is not None:
    print(store + "\t" + str(highestSale))
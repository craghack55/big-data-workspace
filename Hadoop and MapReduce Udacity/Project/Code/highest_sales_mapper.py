#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split('\t')

    store, sale = data[2], data[4]
    
    print(store + "\t" + sale)
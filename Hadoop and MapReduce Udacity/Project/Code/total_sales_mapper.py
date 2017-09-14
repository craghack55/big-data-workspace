#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split('\t')

    sale = data[4]
    
    print(sale + "\t" + "1")
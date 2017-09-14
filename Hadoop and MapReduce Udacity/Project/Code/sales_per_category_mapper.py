#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split('\t')

    category, sales = data[3], data[4]
    
    print(category + "\t" + sales)
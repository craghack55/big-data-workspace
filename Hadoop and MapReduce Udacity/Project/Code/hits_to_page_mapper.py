#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    page = data[6]
    
    print(page + "\t" + "1")
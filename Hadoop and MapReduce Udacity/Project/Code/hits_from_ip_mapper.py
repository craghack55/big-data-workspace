#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    ip = data[0]
    
    print(ip + "\t" + "1")
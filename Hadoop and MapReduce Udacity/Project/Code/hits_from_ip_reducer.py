#!/usr/bin/python

import sys

oldKey = None
hit = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    ip, count = data
    count = int(count)
    
    if oldKey is not None and oldKey != ip:
        print(oldKey + "\t" + str(hit))
        hit = 0
        
    hit += count
    oldKey = ip
    
if oldKey is not None:
    print(ip + "\t" + str(hit))
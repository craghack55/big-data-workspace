#!/usr/bin/python

import sys

oldKey = None
visited = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    page, count = data
    count = int(count)
    
    if oldKey is not None and oldKey != page:
        print(oldKey + "\t" + str(visited))
        visited = 0.0
        
    visited += count
    oldKey = page
    
if oldKey is not None:
    print(page + "\t" + str(visited))
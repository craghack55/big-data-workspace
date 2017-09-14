#!/usr/bin/python

import sys

oldKey = None
visited = 0
mostVisited = 0
mostVisitedPage = ""

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        continue
    
    page, count = data
    count = int(count)
    
    if oldKey is not None and oldKey != page:
        if visited > mostVisited:
            mostVisited = visited
            mostVisitedPage = oldKey
            
        visited = 0
        
    visited += count
    oldKey = page
    
if oldKey is not None:
    if visited > mostVisited:
        mostVisited = visited
        mostVisitedPage = page
        
print(mostVisitedPage + "\t" + str(mostVisited))
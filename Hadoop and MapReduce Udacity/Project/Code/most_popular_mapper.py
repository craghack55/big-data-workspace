#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    page = data[6]
    
    if data[6].startswith("http://www.the-associates.co.uk"):
        page = data[6].replace("http://www.the-associates.co.uk", "")

    print(page + "\t" + "1")
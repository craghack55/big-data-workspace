import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader)

for line in reader:
    if len(line) == 19:
        qNodeID = line[0]
        nodeType = line[5]
        authorID = line[3]
        
        if nodeType == "answer":
            qNodeID = line[6]
        elif nodeType == "comment":
            qNodeID = line[7]
        
        print(qNodeID + '\t' + authorID)
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader)

for line in reader:
    if len(line) == 19:
        qNodeID = line[0]
        bLength = str(len(line[4]))
        nodeType = line[5]
        
        if nodeType == "question":
            parentID = "-1"
        elif nodeType == "answer":
            parentID = line[6]
            qNodeID = parentID
        
        print(qNodeID + '\t' + bLength + '\t' + parentID)
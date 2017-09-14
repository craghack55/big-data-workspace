import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader)

for line in reader:
    if len(line) == 19:
        authorID = line[3]
        hour = line[8].strip()[11 : 13]
        
        print(authorID + '\t' + str(int(hour)))
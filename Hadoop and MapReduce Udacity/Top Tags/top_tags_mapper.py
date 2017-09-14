import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
next(reader)

for line in reader:
    if len(line) == 19 and line[5] == "question":
        tags = line[2].split(" ")
        for t in tags:
            print(t + "\t" + "1")
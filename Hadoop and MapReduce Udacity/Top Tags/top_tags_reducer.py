import sys

oldKey = None
count = 0
temp = []

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue
    
    tag = data[0]
    
    if oldKey is not None and oldKey != tag:
        temp.append((oldKey, count))
        count = 0
    
    oldKey = tag
    count += 1
    
if oldKey is not None:
    temp.append((tag, count))
    
sortedByCount = sorted(temp, key = lambda tup: tup[1], reverse = True)

for i in range(0, 10):
    t = sortedByCount[i][0]
    c = sortedByCount[i][1]
    print(t + "\t" + str(c))
import sys

hoursCounter = [0] * 24
oldKey = None

def addEntry(hour, hoursCounter):
    hoursCounter[int(hour)] += 1
    
def getHighest(hoursCounter):
    result = []
    maxHour = max(hoursCounter)
    
    for i in range(0, len(hoursCounter)):
        if hoursCounter[i] == maxHour:
            result.append(str(i))
            
    return result

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue
    
    authorID, hour = data
        
    if oldKey is not None and oldKey != authorID:
        highest = getHighest(hoursCounter)
        
        for i in highest:
            print(oldKey + "\t" + i)
        
        hoursCounter = [0] * 24
        
    oldKey = authorID
    addEntry(hour, hoursCounter)
    
if oldKey is not None:
    highest = getHighest(hoursCounter)
    for i in highest:
        print(authorID + "\t" + i)
    
    
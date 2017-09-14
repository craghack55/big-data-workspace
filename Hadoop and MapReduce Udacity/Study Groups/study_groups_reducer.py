import sys

oldKey = None
students = []

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 2:
        continue
    
    qNodeID, authorID = data
    
    if oldKey is not None and oldKey != qNodeID:
        print(oldKey + "\t" + '[%s]' % ', '.join(map(str, students)))
        students = []
        
    if authorID not in students:
        students.append(authorID)
        
    oldKey = qNodeID
    
if oldKey is not None:
    print(qNodeID + "\t" + '[%s]' % ', '.join(map(str, students)))

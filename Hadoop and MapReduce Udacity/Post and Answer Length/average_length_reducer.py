import sys

oldKey = None
qLength = -1
numOfAnswers = 0
sumOfAnswerLenghts = 0

def getAverageAnswerLength(numOfAnswers, sumOfAnswerLength):
    if numOfAnswers == 0:
        return "0"
    else:
        return str(sumOfAnswerLength / numOfAnswers)

for line in sys.stdin:
    data = line.strip().split('\t')
    
    if len(data) != 3:
        continue
    
    qNodeID, bLength, parentID = data
    bLength = int(bLength)
    
    if oldKey is not None and oldKey != qNodeID:
        print(oldKey + "\t" + str(qLength) + "\t" + getAverageAnswerLength(numOfAnswers, sumOfAnswerLenghts))
        qLength = -1
        numOfAnswers = 0
        sumOfAnswerLenghts = 0
        
    
    if parentID == "-1":
        qLength = bLength
    else:
        numOfAnswers += 1
        sumOfAnswerLenghts += bLength
        
    oldKey = qNodeID
    
if oldKey is not None:
    print(qNodeID + "\t", str(qLength) + "\t" + getAverageAnswerLength(numOfAnswers, sumOfAnswerLenghts))
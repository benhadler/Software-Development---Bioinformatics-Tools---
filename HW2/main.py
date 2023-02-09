import sys
sys.setrecursionlimit(1500)
import random
def align(first, second, match, mismatch, indel):
    maximum = []
    bt = []
    for i in range(len(first) + 1):
        maximum.insert(i,[])
        bt.insert(i,[])
    # print(maximum)
    maximum[0].insert(0,0)
    bt[0].insert(0,3)
    for i in range(1,len(first) + 1):
        maximum[i].insert(0,0)
        bt[i].insert(0,3)
    for i in range(1,len(second) + 1):
        maximum[0].insert(i,0)
        bt[0].insert(i,3)
    for i in range(1,len(first) + 1):
        for j in range(1,len(second) + 1):
            # print("i = ",i)
            # print('j = ',j)
            if first[i - 1] == second[j - 1]:
                matching = True
            else:
                matching = False
            fromBeg = 0
            fromTop = maximum[i - 1][j] - indel
            fromLeft = maximum[i][j - 1] - indel
            fromCross = ''
            if matching:
                fromCross = maximum[i-1][j-1] + match
            else:
                fromCross = maximum[i - 1][j - 1] - mismatch
            maximum[i].insert(j,max(fromBeg,fromTop,fromLeft,fromCross))
            if maximum[i][j] == fromTop:
                bt[i].insert(j,0)
            elif maximum[i][j] == fromLeft:
                bt[i].insert(j,1)
            elif maximum[i][j] == fromCross:
                bt[i].insert(j,2)
            else:
                bt[i].insert(j,3)
    maxScore = -9999999
    iIndex = -1
    jIndex = -1
    for i in range(len(first) + 1):
        for j in range(len(second) + 1):
            if maximum[i][j] > maxScore:
                maxScore = maximum[i][j]
                iIndex = i
                jIndex = j
    answers = [maxScore,bt,iIndex,jIndex]
    return answers
def getTopString(first, bt, iIndex, jIndex):
    if iIndex == 0 or jIndex == 0:
        return ''
    if bt[iIndex][jIndex] == 0:
        return getTopString(first, bt, iIndex - 1, jIndex) + first[iIndex - 1]
    elif bt[iIndex][jIndex] == 1:
        return getTopString(first, bt, iIndex, jIndex - 1)+ '-'
    elif bt[iIndex][jIndex] == 2:
        return getTopString(first, bt, iIndex - 1, jIndex - 1) + first[iIndex - 1]
    else:
        return ''
def getBotString(second, bt, iIndex, jIndex):
    if iIndex == 0 or jIndex == 0:
        return ''
    if bt[iIndex][jIndex] == 0:
        return getBotString(second, bt, iIndex - 1, jIndex) + '-'
    elif bt[iIndex][jIndex] == 1:
        return getBotString(second, bt, iIndex, jIndex - 1) + second[jIndex - 1]
    elif bt[iIndex][jIndex] == 2:
        return getBotString(second, bt, iIndex - 1, jIndex - 1) + second[jIndex - 1]
    else:
        return ''
def getMidString(first, second,bt,iIndex,jIndex):
    if iIndex == 0 or jIndex == 0:
        return ''
    if bt[iIndex][jIndex] == 0:
        return getMidString(first, second,bt, iIndex - 1, jIndex) + ' '
    elif bt[iIndex][jIndex] == 1:
        return getMidString(first, second, bt, iIndex, jIndex - 1) + ' '
    elif bt[iIndex][jIndex] == 2:
        if first[iIndex - 1] == second[jIndex - 1]:
            return getMidString(first, second, bt, iIndex - 1, jIndex - 1) + '|'
        else:
            return getMidString(first, second, bt, iIndex - 1, jIndex - 1) + ' '
    else:
        return ''

def randSequence(seqLength):
    sequence = ''
    for i in range(seqLength):
        value = random.randint(1, 4)
        if value == 1:
            sequence = sequence + 'A'
        elif value == 2:
            sequence = sequence + 'T'
        elif value == 3:
            sequence = sequence + 'C'
        else:
            sequence = sequence + 'G'
    return sequence
def getAvgAlnLenth(numPairs, numChars, match, mismatch, indel):
    lengthSum = 0
    for i in range(numPairs):
        sequence1 = randSequence(numChars)
        sequence2 = randSequence(numChars)
        answers = align(sequence1,sequence2,match, mismatch, indel)
        alignment = getTopString(sequence1, answers[1], answers[2], answers[3])
        lengthSum = lengthSum + len(alignment)
    return lengthSum / numPairs
def findMax(first, second, match, mismatch, indel):
    maxI = -1
    maxJ = -1
    maxScore = -1
    scores = [[],[]]
    scores[0].insert(0,0)
    for j in range(1,len(second) + 1):
        scores[0].insert(j,0)
    for i in range(1,len(first) + 1):
        # print(i)
        fromTop = scores[0][0] - indel
        scores[1].insert(0,max(fromTop,0))
        for j in range(1, len(second) + 1):
            fromTop = scores[0][j] - indel
            fromLeft = scores[1][j - 1] - indel
            if first[i - 1] == second[j - 1]:
                fromCross = scores[0][j - 1] + match
            else:
                fromCross = scores[0][j - 1] - mismatch
            scores[1].insert(j,max(fromTop,fromLeft,fromCross,0))
            if scores[1][j] > maxScore:
                maxScore = scores[1][j]
                maxI = i
                maxJ = j
        scores.pop(0)
        scores.insert(1,[])
    answers = [maxI,maxJ,maxScore]
    return answers

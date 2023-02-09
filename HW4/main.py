# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from freqs import *
import math
# x = '1'
# y = 1
# print (int(x) + y)
#
# str = '28735 29810'
# nums = str.split(' ')
# print(nums)
answers = freqReport2('chrA.fasta')
dnaSeq = answers[3]
non_Island = ''
island = ''
nums = []
## make two strings: one for CPG islands and one for non-CPG islands.
with open('chrA.islands') as infile:
    prev = 0
    for line in infile:
        nums = line.split(' ')
        non_Island = non_Island + dnaSeq[prev:int(nums[0])]
        prev = int(nums[1])
        island = island + dnaSeq[int(nums[0]):int(nums[1])]
    non_Island = non_Island + dnaSeq[prev:len(dnaSeq)]
ansNonIsland = freqReport3(non_Island)
ansIsland = freqReport3(island)
## These two dictionaries will serve as transition frequencies.
transFreqsIslands = {}
transFreqsNonIslands = {}
totFreqA = 0
totFreqT = 0
totFreqC = 0
totFreqG = 0
## Get sum of Frequencies transitioning FROM each nucleotide
for i in range(16):
    if i < 4:
        totFreqA = totFreqA + ansNonIsland[2][i]
    elif i < 8:
        totFreqT = totFreqT + ansNonIsland[2][i]
    elif i < 12:
        totFreqC = totFreqC + ansNonIsland[2][i]
    else:
        totFreqG = totFreqG + ansNonIsland[2][i]
## Divide specific Transition by all transitions from that nucleotide to get specific transition frequency
for i in range(16):
    if i < 4:
        transFreqsNonIslands[ansNonIsland[0][i]] = ansNonIsland[2][i] / totFreqA
    elif i < 8:
        transFreqsNonIslands[ansNonIsland[0][i]] = ansNonIsland[2][i] / totFreqT
    elif i < 12:
        transFreqsNonIslands[ansNonIsland[0][i]] = ansNonIsland[2][i] / totFreqC
    else:
        transFreqsNonIslands[ansNonIsland[0][i]] = ansNonIsland[2][i] / totFreqG
print(transFreqsNonIslands)
## repeat for Islands
totFreqA = 0
totFreqT = 0
totFreqC = 0
totFreqG = 0
for i in range(16):
    if i < 4:
        totFreqA = totFreqA + ansIsland[2][i]
    elif i < 8:
        totFreqT = totFreqT + ansIsland[2][i]
    elif i < 12:
        totFreqC = totFreqC + ansIsland[2][i]
    else:
        totFreqG = totFreqG + ansIsland[2][i]
for i in range(16):
    if i < 4:
        transFreqsIslands[ansIsland[0][i]] = ansIsland[2][i] / totFreqA
    elif i < 8:
        transFreqsIslands[ansIsland[0][i]] = ansIsland[2][i] / totFreqT
    elif i < 12:
        transFreqsIslands[ansIsland[0][i]] = ansIsland[2][i] / totFreqC
    else:
        transFreqsIslands[ansIsland[0][i]] = ansIsland[2][i] / totFreqG
## Use dictionary of transition probs to get prob of a sequence
def getProbOfSeq(transFreqs, seq):
    prob = .25
    for i in range(len(seq) - 1):
        transition = seq[i:i + 2]
        prob = prob * transFreqs.get(transition)
    return prob
## CpG potential score as outlined in homework pdf
def getScoreOfSeq(nTransFreqs,iTransFreqs,start,end,seq):
    probNonCPG = getProbOfSeq(nTransFreqs,seq[start:end])
    probCPG = getProbOfSeq(iTransFreqs, seq[start:end])
    score = probCPG / probNonCPG
    score = math.log2(score)
    return score
predictedIslands = ''
index = 0
islandCurrently = False
print(len(dnaSeq))
while index + 100 < len(dnaSeq):
    #if Island,
    if(getScoreOfSeq(transFreqsNonIslands,transFreqsIslands,index, index + 100,dnaSeq) > 0):
        if islandCurrently:
            index = index + 100
            continue
        else:
            islandCurrently = True
            predictedIslands = predictedIslands + str(index) + ' '
            index = index + 100
    else:
        if islandCurrently:
            predictedIslands = predictedIslands + str(index)
            newLineChar = '\n'
            predictedIslands = predictedIslands + newLineChar
            islandCurrently = False
            index = index + 100
        else:
            index = index + 100
            continue
print(predictedIslands)
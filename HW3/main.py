# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from trie import *
from eVals import *
trie = trie('queries2.txt')
with open ('DNA.txt') as infile:
    for line in infile:
        if line[0] != '>':
            nextLine = line.strip('\n')
            sequence += nextLine
sequence = sequence.strip('\n')
with open('queries2.txt') as infile:
    freqs = getFreqs(sequence)
    seqs = []
    count = []
    expected = []
    for line in infile:
        str = line.strip("\n")
        seqs.insert(len(seqs),str)
        count.insert(len(count),0)
        expected.insert(len(expected),getE(line,freqs,len(sequence)))

# print(len(sequence))
for i in range(0,len(sequence)):
    index = findNum(trie,sequence[i:i + 50])
    # print(index)
    if index != -1 and index != None:
        count[index] = count[index] + 1
for i in range(len(seqs)):
    print(f"{seqs[i]} - Expected: {expected[i]} Found: {count[i]}")
# print(sequence)
# with open('queries2.txt') as ex:
#     for line in ex:
#
#         print(findNum(trie,line))
# print(findNum(trie,'AATAGCTAACA'))
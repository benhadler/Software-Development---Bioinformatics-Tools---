from main import *
import argparse
sys.setrecursionlimit(1500)
parser = argparse.ArgumentParser(description='Find the Local Alignment of two sequences')
parser.add_argument('seq_files', type=str, help ='Name of File')
parser.add_argument('-m', '--match', type = float, required = True, help = 'match-score')
parser.add_argument('-s', '--mismatch', type = float, required = True, help = 'mismatch-score')
parser.add_argument('-d', '--indel', type = float, required = True, help = 'indel')
parser.add_argument('-a','--alignment',help = 'print alignment', action = 'store_true')
args = parser.parse_args()
seqs = []
with open (args.seq_files) as infile:
    for line in infile:
        if line[0] == 'A' or line[0] == 'T' or line[0] == 'C' or line[0] == 'G':
            sequence = line.strip('\n')
            seqs.insert(len(seqs),sequence)

first = seqs[0]
second = seqs[1]
answersFirst = findMax(first,second,args.match,args.mismatch,args.indel)
revFirst = first[:answersFirst[0]]
revFirst = revFirst[::-1]
revSecond = second[:answersFirst[1]]
revSecond = revSecond[::-1]
answersSecond = findMax(revFirst,revSecond,args.match,args.mismatch,args.indel)
finalFirst = first[answersFirst[0] - answersSecond[0]:answersFirst[0]]
finalSecond = second[answersFirst[1] - answersSecond[1]:answersFirst[1]]
answersThird = align(finalFirst,finalSecond,args.match, args.mismatch, args.indel)
topStr = getTopString(finalFirst,answersThird[1],answersThird[2],answersThird[3])
print(len(topStr))
print(answersFirst[2])
if(args.alignment):
    print(topStr)
    print(getMidString(finalFirst,finalSecond,answersThird[1],answersThird[2],answersThird[3]))
    print(getBotString(finalSecond,answersThird[1],answersThird[2],answersThird[3]))
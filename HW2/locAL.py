import argparse
from main import *
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
answers = align(first,second,args.match, args.mismatch, args.indel)
print(answers[0])
firstAlignedSeq = getTopString(first,answers[1],answers[2],answers[3])
print(len(firstAlignedSeq))
if args.alignment:
    secondAlignedSeq = getBotString(second, answers[1],answers[2],answers[3])
    midSeq = getMidString(first, second, answers[1],answers[2],answers[3])
    print(firstAlignedSeq)
    print(midSeq)
    print(secondAlignedSeq)
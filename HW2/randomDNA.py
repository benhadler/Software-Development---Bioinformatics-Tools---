import argparse
import random
parser = argparse.ArgumentParser(description='Generate Random DNA Sequences')
parser.add_argument('num_seq', type=int, help ='Number of Sequences')
parser.add_argument('len_seq', type=int, help ='Length of Sequences')
args = parser.parse_args()
numA = 0
numT = 0
numC = 0
numG = 0
for i in range(args.num_seq):
    sequence = ''
    for j in range(args.len_seq):
        value=random.randint(1,4)
        if value == 1:
            sequence = sequence + 'A'
            numA = numA + 1
        elif value == 2:
            sequence = sequence + 'T'
            numT = numT + 1
        elif value == 3:
            sequence = sequence + 'C'
            numC = numC + 1
        else:
            sequence = sequence + 'G'
            numG = numG + 1
    print(sequence)
print('Nucleotide Frequencies:')
totNuc = args.num_seq * args.len_seq
print('A:', numA / totNuc)
print('T:', numT / totNuc)
print('C:', numC / totNuc)
print('G:', numG / totNuc)
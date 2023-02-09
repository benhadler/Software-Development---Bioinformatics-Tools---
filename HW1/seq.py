import sys
with open(sys.argv[1]) as infile:
    sequence = ''
    first = True
    for line in infile:
        if line[0] == '>':
            if first:
                first = False
            else:
                sequence = sequence + '@'
        else:
            sequence += line
    sequence = sequence.replace('\n','')
    sequence = sequence.rstrip("\n")
    print(sequence)
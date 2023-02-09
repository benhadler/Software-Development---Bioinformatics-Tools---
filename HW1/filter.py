import sys


def print60(seq):
    for i in range(len(seq)):
        if (i % 60) == 0 and i != 0:
            print('')
            print('')
        print(seq[i], end='')
    if len(seq) != 60:
        print('')
def print60noLine(seq):
    for i in range(len(seq)):
        if (i % 60) == 0 and i != 0:
            print('')
            print('')
        print(seq[i], end='')


with open(sys.argv[1]) as infile:
    sequence = ''
    reading = False
    first = True
    count = 0
    prev = False
    for line in infile:
        if line[0] == '>':
            if line.find('Mus musculus') != -1 or line.find('Rattus norvegicus') != -1:
                if reading == True:
                    prev = True
                else:
                    prev = False
                reading = True
                if first:
                    first = False
                    newLine = line.replace('\n','')
                    print(newLine)
                    print()
                else:
                    sequence = sequence.replace('\n', '')
                    print60(sequence)
                    if prev:
                        print()
                    sequence = ''
                    newLine = line.replace('\n', '')
                    print(newLine)
                    print()
            elif reading:
                sequence = sequence.replace('\n', '')
                print60(sequence)
                sequence = ''
                reading = False
        elif reading:
            sequence += line
    sequence = sequence.replace('\n', "")
    print60noLine(sequence)

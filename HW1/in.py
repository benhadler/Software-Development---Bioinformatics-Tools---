import sys
with open(sys.argv[1]) as infile:
    f = open(sys.argv[2],"w")
    sequence = ''
    first = True
    for line in infile:
        if line[0] == '>':
            if first:
                fileTxt = line[4:11]
                fileTxt += " "+ str(len(sequence)) + "\n"
                first = False
            else:
                fileTxt += line[4:11]
                fileTxt += " " + str(len(sequence)) + "\n"
        else:
            sequence += line
            sequence = sequence.replace('\n', '')
    fileTxt = fileTxt.rstrip('\n')
    f.write(fileTxt)

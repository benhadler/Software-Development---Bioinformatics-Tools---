import sys

with open(sys.argv[1]) as infile:
    for line in infile:
        sequence = line
position = line.find(sys.argv[3])
with open(sys.argv[2]) as infile2:
    first = True
    for line2 in infile2:
        if first:
            first = False
            prev = line2[0:7]
        else:
            if int(line2[8:]) > position:
                print(prev)
                quit()
            else:
                prev = line2[0:7]
print(prev)
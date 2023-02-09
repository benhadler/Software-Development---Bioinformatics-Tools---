import sys
with open(sys.argv[1]) as infile:
    first = True
    count = 0
    for line in infile:
        if line[0]=='>':
            if first == True:
                first = False
            else:
                print(count)
                count = 0
            print(line.strip())
        else:
            if len(line) == 1:
                continue
            count += len(line)
            count -= 1
    print(count)

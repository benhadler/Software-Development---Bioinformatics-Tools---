dna = ''
with open ('DNA.txt') as infile:
    for line in infile:
        if line[0] != '>':
            nextLine = line.strip('\n')
            dna += nextLine
dna = dna.strip('\n')
def getFreqs(sequence):
    freqs = [0,0,0,0]
    for i in range(len(sequence)):
        if sequence[i] == 'A':
            freqs[0] = freqs[0] + 1
        elif sequence[i] == 'T':
            freqs[1] = freqs[1] + 1
        elif sequence[i] == 'C':
            freqs[2] = freqs[2] + 1
        else:
            freqs[3] = freqs[3] + 1
    for i in range(4):
        freqs[i] = freqs[i] / len(sequence)
    return freqs
def getProb(query, freqs):
    counts = [0, 0, 0, 0]
    for i in range(len(query)):
        if query[i] == 'A':
            counts[0] = counts[0] + 1
        elif query[i] == 'T':
            counts[1] = counts[1] + 1
        elif query[i] == 'C':
            counts[2] = counts[2] + 1
        else:
            counts[3] = counts[3] + 1
    return ((freqs[0] ** counts[0]) * (freqs[1] ** counts[1]) * (freqs[2] ** counts[2]) * (freqs[3] ** counts[3]))
def getE(query,freqs,length):
    return getProb(query,freqs) * (length - len(query) + 1)

# freqs = getFreqs(dna)
# print(freqs)
# print(len(dna))
# print(getProb('GCCGCCTTCACATTCTCAAAGGAACTCCTGGCCCCCAAACAGGGTCCGGG',freqs))
# print(getE('GCCGCCTTCACATTCTCAAAGGAACTCCTGGCCCCCAAACAGGGTCCGGG',freqs, len(dna)))
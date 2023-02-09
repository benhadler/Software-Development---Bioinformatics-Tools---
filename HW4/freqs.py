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
def getSeq(file):
    seq = ''
    with open(file) as infile:
        for line in infile:
            if line[0] != '>':
                str = line.strip("\n")
                seq = seq + str
    return seq
def eFreqs(freqs):
    eFreqs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    eFreqs[0] = freqs[0] * freqs[0]
    eFreqs[1] = freqs[0] * freqs[1]
    eFreqs[2] = freqs[0] * freqs[2]
    eFreqs[3] = freqs[0] * freqs[3]
    eFreqs[4] = freqs[1] * freqs[0]
    eFreqs[5] = freqs[1] * freqs[1]
    eFreqs[6] = freqs[1] * freqs[2]
    eFreqs[7] = freqs[1] * freqs[3]
    eFreqs[8] = freqs[2] * freqs[0]
    eFreqs[9] = freqs[2] * freqs[1]
    eFreqs[10] = freqs[2] * freqs[2]
    eFreqs[11] = freqs[2] * freqs[3]
    eFreqs[12] = freqs[3] * freqs[0]
    eFreqs[13] = freqs[3] * freqs[1]
    eFreqs[14] = freqs[3] * freqs[2]
    eFreqs[15] = freqs[3] * freqs[3]
    return eFreqs
def oFreqs(seq):
    oFreqs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(seq) - 1):
        diNuc = seq[i:i+2]
        # if i % 100000 == 0:
        #     print(diNuc)
        if diNuc == 'AA':
            oFreqs[0] = oFreqs[0] + 1
        elif diNuc =='AT':
            oFreqs[1] = oFreqs[1] + 1
        elif diNuc =='AC':
            oFreqs[2] = oFreqs[2] + 1
        elif diNuc =='AG':
            oFreqs[3] = oFreqs[3] + 1
        elif diNuc =='TA':
            oFreqs[4] = oFreqs[4] + 1
        elif diNuc =='TT':
            oFreqs[5] = oFreqs[5] + 1
        elif diNuc =='TC':
            oFreqs[6] = oFreqs[6] + 1
        elif diNuc =='TG':
            oFreqs[7] = oFreqs[7] + 1
        elif diNuc =='CA':
            oFreqs[8] = oFreqs[8] + 1
        elif diNuc =='CT':
            oFreqs[9] = oFreqs[9] + 1
        elif diNuc =='CC':
            oFreqs[10] = oFreqs[10] + 1
        elif diNuc =='CG':
            oFreqs[11] = oFreqs[11] + 1
        elif diNuc =='GA':
            oFreqs[12] = oFreqs[12] + 1
        elif diNuc =='GT':
            oFreqs[13] = oFreqs[13] + 1
        elif diNuc =='GC':
            oFreqs[14] = oFreqs[14] + 1
        elif diNuc =='GG':
            oFreqs[15] = oFreqs[15] + 1
    for i in range(16):
        oFreqs[i] = oFreqs[i] / (len(seq) - 1)
    return oFreqs
def freqReport(file):
    diNucs = ['AA','AT','AC','AG','TA','TT','TC','TG','CA','CT','CC','CG','GA','GT','GC','GG']
    seq = getSeq(file)
    expectedFreqs = eFreqs(getFreqs(seq))
    observedFreqs = oFreqs(seq)
    for i in range(16):
        print(f'{diNucs[i]} - Expected: {expectedFreqs[i]} Observed: {observedFreqs[i]}')
def freqReport2(file):
    diNucs = ['AA', 'AT', 'AC', 'AG', 'TA', 'TT', 'TC', 'TG', 'CA', 'CT', 'CC', 'CG', 'GA', 'GT', 'GC', 'GG']
    seq = getSeq(file)
    expectedFreqs = eFreqs(getFreqs(seq))
    observedFreqs = oFreqs(seq)
    return [diNucs,expectedFreqs, observedFreqs, seq]
def freqReport3(seq):
    diNucs = ['AA', 'AT', 'AC', 'AG', 'TA', 'TT', 'TC', 'TG', 'CA', 'CT', 'CC', 'CG', 'GA', 'GT', 'GC', 'GG']
    expectedFreqs = eFreqs(getFreqs(seq))
    observedFreqs = oFreqs(seq)
    return [diNucs, expectedFreqs, observedFreqs, seq]

# freqReport('chrA.fasta')
# sum = 0
# dnaSeq = getSeq('chrA.fasta')
# expectedFreqs = eFreqs(getFreqs(dnaSeq))
# observedFreqs = oFreqs(dnaSeq)
# for i in range (16):
#     sum = sum + (((expectedFreqs[i] * len(dnaSeq) - observedFreqs[i] * len(dnaSeq)) *  (expectedFreqs[i] * len(dnaSeq) - observedFreqs[i] * len(dnaSeq))) / (expectedFreqs[i] * len(dnaSeq)))
# print('Chi-squared value:',sum)
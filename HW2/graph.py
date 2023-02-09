from matplotlib import pyplot as plt
from main import *
import random

P1_length = 0
P2_length = 0
lengths1 = []
lengths2 = []
avg_lengths = []
# Change number of iteration for number of read pairs aligned
for i in range(500):
   sequence1 = ''
   for j in range(1000):
       value = random.randint(1, 4)
       if value == 1:
           sequence1 = sequence1 + 'A'
       elif value == 2:
           sequence1 = sequence1 + 'T'
       elif value == 3:
           sequence1 = sequence1 + 'C'
       else:
           sequence1 = sequence1 + 'G'
   sequence2 = ""
   # Change number of iterations to match desired read length
   for j in range(1000):
       value = random.randint(1, 4)
       if value == 1:
           sequence2 = sequence2 + 'A'
       elif value == 2:
           sequence2 = sequence2 + 'T'
       elif value == 3:
           sequence2 = sequence2 + 'C'
       else:
           sequence2 = sequence2 + 'G'
   #Align according to different parameters
   ans1 = align(sequence1, sequence2, 1, 10, 0)
   alignment1 = getTopString(sequence1, ans1[1], ans1[2], ans1[3])
   P1_length = P1_length + len(alignment1)
   lengths1.insert(len(alignment1), len(alignment1))
   ans2 = align(sequence1, sequence2, 1, 30, 20)
   alignment2 = getTopString(sequence1, ans2[1], ans2[2], ans2[3])
   P2_length = P2_length + len(alignment2)
   lengths2.insert(len(alignment2), len(alignment2))
   # avg_lengths.insert(len(avg_lengths),(P2_length / 5))
plt.title('Length of Alignments')
plt.xlabel('Length (bp)')
plt.ylabel('Number of Reads')
plt.hist(lengths1)
plt.hist(lengths2)
plt.show()

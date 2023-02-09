from matplotlib import pyplot as plt
import sys
from main import *
sys.setrecursionlimit(10000)

# First Graph

x = [-30, -20, -10, -1, -0.5, -0.33, -0.25, 0]
h = []
for int in x:
    h.insert(len(h), getAvgAlnLenth(10,1000,1,-1 * int,-1 * int))
plt.bar(x,h,width= .1)
plt.title('lP(1000) For Different Parameter Sets')
plt.xlabel('Penalty For Indels and Mismatches')
plt.ylabel('Average Local Alignment Length')
plt.show()

# Second Graph

x = [-1.3,-1.25, -1.2, -1.15, -1.1, -1.05 -1]
h = []
for int in x:
    h.insert(len(h), getAvgAlnLenth(10,1000,1,-1 * int,-1 * int))
plt.bar(x,h, width=.01)
plt.title('lP(1000) For Different Parameter Sets')
plt.xlabel('Penalty For Indels and Mismatches')
plt.ylabel('Average Local Alignment Length')
ax1 = plt.subplot()
ax1.set_xticks(x)
ax1.set_xticklabels(x)
plt.show()

# Third Graph

x = [-1.3,-1.25, -1.2, -1.15, -1.1, -1.05, -1]
h = []
for int in x:
    h.insert(len(h), getAvgAlnLenth(10,1000,1,-1 * int,1))
plt.bar(x,h, width=.01)
plt.title('lP(1000) For Different Mismatch Penalties with Indel Penalty of 1')
plt.xlabel('Penalty For Mismatches')
plt.ylabel('Average Local Alignment Length')
ax1 = plt.subplot()
ax1.set_xticks(x)
ax1.set_xticklabels(x)
plt.show()

# Fourth Graph

x = [-1.5, -1.45, -1.4, -1.35, -1.3,-1.25, -1.2, -1.15, -1.1]
h = []
for int in x:
    h.insert(len(h), getAvgAlnLenth(30,1000,1,1,-1 * int))
plt.bar(x,h, width=.01)
plt.title('lP(1000) For Different Indel Penalties with Mismatch Penalty of 1')
plt.xlabel('Penalty For Indels')
plt.ylabel('Average Local Alignment Length')
ax1 = plt.subplot()
ax1.set_xticks(x)
ax1.set_xticklabels(x)
plt.show()
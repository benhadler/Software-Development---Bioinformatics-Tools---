from matplotlib import pyplot as plt

times = [.0005,.1164,113.4183,.4562,.4498]
sizes = [100,10000,1000000,1000000,1000000]
plt.scatter(sizes,times)
plt.xlabel('Size (entries)')
plt.ylabel('Time (seconds)')
plt.title('Running time as a function of input size')
plt.show()

times2 = [.0005,.1164,113.4183]
sizes2 = [100,10000,1000000]
plt.scatter(sizes2,times2)
plt.xlabel('Size (entries)')
plt.ylabel('Time (seconds)')
plt.title('Running time as a function of input size')
plt.show()
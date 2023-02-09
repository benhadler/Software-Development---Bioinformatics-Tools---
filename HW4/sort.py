import time
class matrix:
    def __init__(self,file):
        currLine = ''
        numLines = 0
        matrix = []
        with open(file) as infile:
            for line in infile:
                currLine = line
                numLines = numLines + 1
            self.numRows = numLines
            self.numCols = len(currLine)
            for i in range(self.numRows):
                matrix.insert(len(matrix),[])
        lineNum = 0
        with open(file) as infile:
            for line in infile:
                # print('got here')
                for i in range(self.numCols):
                    # print('got here')
                    matrix[lineNum].insert(len(matrix[lineNum]),line[i])
                lineNum = lineNum + 1
        self.matrix = matrix
        self.sorted = False
    def printMatrix(self):
        for i in range(self.numRows):
            # print('i =',i)
            # print(len(self.matrix))
            # print(len(self.matrix[0]))
            for j in range(self.numCols):
                # print('j=',j)
                print(self.matrix[i][j], end="")
            print()
    def sort(self):
        if(self.sorted == True):
            return
        zeroBucket = []
        oneBucket = []
        Order = []
        for i in range(self.numCols):
            Order.insert(len(Order),i)
        for i in range(self.numRows):
            for j in range(len(Order)):
                if self.matrix[self.numRows - i - 1][Order[j]] == '0':
                    zeroBucket.insert(len(zeroBucket),Order[j])
                else:
                    oneBucket.insert(len(oneBucket),Order[j])
            Order.clear()
            for j in range(len(oneBucket)):
                Order.insert(len(Order),oneBucket[j])
            for j in range(len(zeroBucket)):
                Order.insert(len(Order),zeroBucket[j])
            # print('zeroBucket:', zeroBucket)
            # print('oneBucket:', oneBucket)
            # print('Order:', Order)
            zeroBucket.clear()
            oneBucket.clear()
        newMatrix = []
        for i in range(self.numRows):
            newMatrix.insert(len(newMatrix),[])
        for i in range(self.numRows):
            # print('i:',i)
            for j in range(self.numCols):
                # print('j:',j)
                newMatrix[i].insert(len(newMatrix),self.matrix[i][Order[j]])
        self.sorted = True
        self.matrix = newMatrix
    def checkCols(self,first,second):
        secondUnderFirst = False
        firstUnderSecond = False
        matching = False
        for i in range(self.numRows):
            if self.matrix[i][first] == '1' and self.matrix[i][second] == '1':
                matching = True
            if self.matrix[i][first] == '1' and self.matrix[i][second] == '0':
                secondUnderFirst = True
            elif self.matrix[i][first] == '0' and self.matrix[i][second] == '1':
                firstUnderSecond = True
            if firstUnderSecond == True and secondUnderFirst == True and matching:
                return False
        return True
    def checkPerfectPhylo(self):
        if self.sorted == False:
            self.sort()
        for i in range(self.numCols):
            for j in range(i):
                if self.checkCols(i,j) == False:
                    # print(i,j)
                    return False
        return True
myMatrix = matrix('a1data1.txt')
print(myMatrix.numRows * myMatrix.numCols)
a = time.perf_counter()
print(myMatrix.checkPerfectPhylo())
b = time.perf_counter()
print(b - a)
myMatrix = matrix('a1data2.txt')
print(myMatrix.numRows * myMatrix.numCols)
a = time.perf_counter()
print(myMatrix.checkPerfectPhylo())
b = time.perf_counter()
print(b - a)
myMatrix = matrix('a1data3.txt')
print(myMatrix.numRows * myMatrix.numCols)
a = time.perf_counter()
print(myMatrix.checkPerfectPhylo())
b = time.perf_counter()
print(b - a)
myMatrix = matrix('a1data4.txt')
print(myMatrix.numRows * myMatrix.numCols)
a = time.perf_counter()
print(myMatrix.checkPerfectPhylo())
b = time.perf_counter()
print(b - a)
myMatrix = matrix('a1data5.txt')
print(myMatrix.numRows * myMatrix.numCols)
a = time.perf_counter()
print(myMatrix.checkPerfectPhylo())
b = time.perf_counter()
print(b - a)
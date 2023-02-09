sequence = ''
# with open ('DNA.txt') as infile:
#     for line in infile:
#         if line[0] != '>':
#             nextLine = line.strip('\n')
#             sequence += nextLine
class trie:

        self.root = Node(None, -1)
        lineNum = -1
        # Create trie from file with strings
        with open(file) as infile:
            for line in infile:
                lineNum = lineNum + 1
                str = line.strip('\n')
                currNode = self.root
                for i in range(len(str)):
                    # print(i,str[i])
                    found = False
                    for next in currNode.nexts:
                        if next.char == str[i]:
                            currNode = next
                            found = True
                            break
                    # if found:
                    #     break
                    # assign Node number of line in file if ending.
                    if i == len(str) - 1 and found == False:
                        newNode = Node(str[i],lineNum)
                        # print("inserted Node",i,"with number",lineNum,'and char',str[i])
                        currNode.nexts.insert(len(currNode.nexts),newNode)
                        currNode = newNode
                    elif found == False:
                        newNode = Node(str[i], -1)
                        currNode.nexts.insert(len(currNode.nexts),newNode)
                        currNode = newNode
class Node:
    def __init__(self,char,num):
        self.char = char
        self.num = num
        self.nexts = []
def findNum(trie, sequence):
    currNode = trie.root
    sequence = sequence.strip('\n')
    for i in range(len(sequence)):
        found = False
        # print(i)
        # print('looking for', sequence[i])
        # print('number of nexts:', len(currNode.nexts))
        for node in currNode.nexts:
            if node.char == sequence[i]:
                currNode = node
                found = True
                # print('found', currNode.char, currNode.num)
                if currNode.num != -1:
                    return currNode.num
                break
        if found == False:
            return -1
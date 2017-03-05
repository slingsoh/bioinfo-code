#!/usr/bin/python

import sys

# read file into an array, where the index +1 = the number that refers to the key
inFile = open('test.txt', 'r')

patterns = []
totLength = 0

for line in inFile:
    line = line.strip()
    totLength += len(line)
    arr = list(line)
    patterns.append(arr)

def main():
    TrieMake(patterns)

def TrieMake(Patterns):
    #currentNode is incoming Node,
    Trie = {} # where key = count, val[0] = symb,
                # val[1] = currentNode
    count = 1
    array = []
    Trie[0] = []
    for pattern in Patterns: # iterates through each string
        currentNode = 0 #starts iteration through trie at root
        list = Trie[0]

        for i in range(1, len(pattern)+1):
            symb = pattern[i-1] #runs through string
            check = False
            list = Trie[currentNode]

            for tup in list: #does currentNode go out to symb
                if tup[0] == symb:
                    check = True
                    y = tup[1]

            if check:
                currentNode = y
            else:
                newNode = count
                Trie[currentNode].append((symb, newNode)) #creates newNode
                triple = (currentNode, newNode, symb) #stores triple for printing later
                array.append(triple)
                currentNode = newNode
                Trie.setdefault(currentNode, [])
                count+=1
    Trie2Adjacency(Trie)



def Trie2Adjacency(Trie):
    for x in Trie:
        for i in Trie.get(x):
            inc = str(x)
            out = str(i[1])
            sym = str(i[0])
            printString = inc + '->' + out +':' + sym
            print printString



if __name__ == '__main__':
    sys.exit(main())

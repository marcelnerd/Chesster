import numpy
import pickle

def writeMoves(arrs, moveFroms, moveTos):
    boardsFile = open("boards.txt", 'wb')
    moveFromsFile = open("moveFroms.txt", 'w')
    moveTosFile = open("moveTos.txt", 'w')

    pickle.dump(arrs, boardsFile, pickle.HIGHEST_PROTOCOL)

    for x in moveFroms:
        moveFromsFile.write(str(x) + "\n")

    for x in moveTos:
        moveTosFile.write(str(x) + "\n")

def readFroms():
    boardsFile = open("boards.txt", 'rb')
    fromsFile = open("moveFroms.txt", 'r')
    boards = []
    froms = []

    boards = pickle.load(boardsFile)

    fromLines = fromsFile.readlines()
    for x in fromLines:
        froms.append(int(x.rstrip("\n")))

    return boards, froms

def readTos():
    boardsFile = open("boards.txt", 'rb')
    tosFile = open("moveTos.txt", 'r')
    boards = []
    tos = []

    boards = pickle.load(boardsFile)

    fromLines = tosFile.readlines()
    for x in fromLines:
        tos.append(int(x.rstrip("\n")))

    return boards, tos

def readBoards():
    return pickle.load(open("boards.txt", 'rb'))




data1 = numpy.zeros((2, 3, 4), dtype=int)
data1[1][1][1] = 34
data2 = [4, 797, 9, 1, 5, 7, 2, 5]
data3 = ['e', 'b', 'c', 'd', 'a', 'f', 'g', 'h', 't', 'j', 'k']

print(data1)
print(data2)
print(data3)

writeMoves(data1, data2, data3)

back1, back2 = readFroms()

print(back1)
print(back2)
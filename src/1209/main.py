import re
from move import Move
from board import Board
import math

DEBUG=False

def getStripedLinesFromFile(fn):
    out=[]
    with open(fn, 'r') as file:
        out=[line.strip('\n') for line in file.readlines()]
    return out

def addTuples(a:tuple, b:tuple):
    return tuple(map(lambda i,j:i+j, a, b))

def parseMoveList(lines):
    return [Move.fromTuple(re.findall("^(R|L|U|D) ([0-9]+)$", line)[0]) for line in lines]

def knotShouldMove(hxy, txy):
    return not all(tuple(map(lambda p1,p2:p1<=p2+1 and p1>=p2-1, txy, hxy)))

def findClosest(hxy, txy):
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    if abs(hxy[0]-txy[0]) >=2 and abs(hxy[1]-txy[1]) >=2:
        directions.extend([(-1,-1), (1, 1), (-1, 1), (1, -1)])
    potentialMoves=[addTuples(hxy, direction) for direction in directions]
    return sorted(potentialMoves, key=lambda p:math.sqrt((p[0]-txy[0])**2 + (p[1]-txy[1])**2))[0]


def executeMoves(moves:list, ropeLength:int)->Board:
    board = Board(ropeLength)
    for move in moves:
        while not move.isDone():
            for i in range(board.getLength()):
                if i==0:
                    board.moveKnot(i, addTuples(board.xy(i), move.getDirection()))
                elif knotShouldMove(board.xy(i-1), board.xy(i)):
                    board.moveKnot(i, findClosest(board.xy(i-1), board.xy(i)))
        if DEBUG:
            print(board)
            print()
        
    return board
            

sampleLines=getStripedLinesFromFile("src/1209/sampleInput.data")
ssampleLines=getStripedLinesFromFile("src/1209/secondSampleInput.data")
lines=getStripedLinesFromFile("src/1209/input.data")

sampleMoves = parseMoveList(sampleLines)
ssampleMoves = parseMoveList(ssampleLines)
moves = parseMoveList(lines)

sampleBoard=executeMoves(sampleMoves, 2)
ssampleBoard=executeMoves(ssampleMoves, 2)
board=executeMoves(moves, 2)

print(len(sampleBoard.getUniqueKnotPositions(-1)))
print(len(ssampleBoard.getUniqueKnotPositions(-1)))
print(len(board.getUniqueKnotPositions(-1)))


sampleMoves = parseMoveList(sampleLines)
ssampleMoves = parseMoveList(ssampleLines)
moves = parseMoveList(lines)

sampleBoard=executeMoves(sampleMoves, 10)
ssampleBoard=executeMoves(ssampleMoves, 10)
board=executeMoves(moves, 10)

print(len(sampleBoard.getUniqueKnotPositions(-1)))
print(len(ssampleBoard.getUniqueKnotPositions(-1)))
print(len(board.getUniqueKnotPositions(-1)))



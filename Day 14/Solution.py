from collections import defaultdict

from enum import Enum
class Cave(Enum):
    AIR  = 1
    ROCK = 2
    SAND = 3

def addTuple(a,b):
    return tuple(map(lambda i, j: i + j, a, b))

def dirTuple(a,b):
    signum = lambda s: 1 if s>0 else -1 if s<0 else 0
    return tuple(map(lambda i, j: signum(j-i), a, b))

def addSand(caveDict,source,bottom):
    if caveDict[source] != Cave.AIR:
        return None

    lastPos,sandPos = None,source
    while sandPos != lastPos:
        if sandPos[1] == bottom-1: # Hit the floor
            return sandPos
        elif caveDict[(pos := addTuple(sandPos,(0,1)))] == Cave.AIR: # Down
            lastPos,sandPos = sandPos,pos
        elif caveDict[(pos := addTuple(sandPos,(-1,1)))] == Cave.AIR: # Down-left
            lastPos,sandPos = sandPos,pos
        elif caveDict[(pos := addTuple(sandPos,(1,1)))] == Cave.AIR: # Down-right
            lastPos,sandPos = sandPos,pos
        else: # Reached rest
            lastPos = sandPos
    return sandPos




def parseData(data):
    caveDict = defaultdict(lambda: Cave.AIR)
    for d in data:
        coords = [tuple(int(x) for x in X.split(',')) for X in d.split(' -> ')]
        for i in range(len(coords)-1):
            dir = dirTuple(coords[i],coords[i+1])
            pos = coords[i]
            while pos != coords[i+1]:
                caveDict[pos] = Cave.ROCK
                pos = addTuple(pos,dir)
        caveDict[coords[-1]] = Cave.ROCK
    bottom = max([int(X.split(',')[1]) for d in data for X in d.split(' -> ')])
    return caveDict, bottom

def Part1(data):
    caveDict, bottom = parseData(data)
    totalSand = 0
    while (s:=addSand(caveDict,(500,0),bottom+2))[1] != bottom+1: # If we hit the floor, it is like entering the abyss
        caveDict[s] = Cave.SAND
        totalSand += 1
    return totalSand

def Part2(data):
    caveDict, bottom = parseData(data)
    totalSand = 0
    while (s:=addSand(caveDict,(500,0),bottom+2)) != None:
        caveDict[s] = Cave.SAND
        totalSand += 1
    return totalSand
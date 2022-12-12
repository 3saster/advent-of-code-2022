from collections import defaultdict
from math import inf

def addTuple(a,b):
    return tuple(map(lambda i, j: i + j, a, b))

def neighbors(elevs):
    neighbors = {k:set() for k in elevs.keys()}
    for e in elevs.keys():
        if   elevs[e] == 'S': elevs[e] = 'a'
        elif elevs[e] == 'E': elevs[e] = 'z'

    for e in elevs.keys():
        if   elevs[e] == 'S': elevs[e] = 'a'
        elif elevs[e] == 'E': elevs[e] = 'z'
        for n in [(0,1),(0,-1),(1,0),(-1,0)]:
            neigh = addTuple(e,n)
            if neigh in elevs.keys() and (ord(elevs[neigh]) - ord(elevs[e])) <= 1:
                neighbors[e].add(neigh)
    return neighbors

def A_Star(graph,start,end,h = lambda n: 0,d = lambda a,b: 1):
    openSet = {start}
    cameFrom = dict()

    gScore = defaultdict(lambda: inf)
    gScore[start] = 0
    fScore = defaultdict(lambda: inf)
    fScore[start] = h(start)

    while len(openSet) > 0:
        current = min(openSet,key=lambda coord: fScore[coord])
        if current == end:
            path = [end]
            while current != start:
                current = cameFrom[current]
                path.append(current) 
            return path[-1::-1]

        openSet.remove(current)
        for neigh in graph[current]:
            tentative_gScore = gScore[current] + d(current,neigh)
            if tentative_gScore < gScore[neigh]:
                cameFrom[neigh] = current
                gScore[neigh] = tentative_gScore
                fScore[neigh] = tentative_gScore + h(neigh)
                openSet.add(neigh)

    return []



def parseData(data):
    locDict = {(ix,iy):i for ix, row in enumerate(data) for iy, i in enumerate(row)}
    start = [k for k,v in locDict.items() if v=='S'][0]
    end = [k for k,v in locDict.items() if v=='E'][0]
    return locDict,start,end

def Part1(data):
    elev, start, end = parseData(data)
    elevGraph = neighbors(elev)
    # On this particular problem, it turns out to be easier to just use Djikstra's (heuristic h(n)=0) than compute the manhattan distance
    path = A_Star(elevGraph,start,end)
    return len(path)-1

def Part2(data):
    elev, start, end = parseData(data)
    elevGraph = neighbors(elev)
    # Possible starts
    starts = {k for k,v in elev.items() if v=='a'}
    # A solution to find the best start is to allow us to freely move between starting points (no cost)
    for s in starts:
        elevGraph[s] = elevGraph[s].union(starts)
        elevGraph[s].remove(s)
    minStart = min([abs(end[1]-n[1]) + abs(end[0]-n[0]) for n in starts])
    # On this particular problem, it turns out to be easier to just use Djikstra's (heuristic h(n)=0) than compute the manhattan distance
    path = A_Star(elevGraph,start,end,d=lambda a,b: 0 if a in starts and b in starts else 1)
    # The 'next' part is the index of the first element that is not a possible start
    return len(path)-next(i for i,p in enumerate(path) if elev[p] != 'a')
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

# When h=0, this is Dijkstra's; when d also equals 1, this is essentially a BFS
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
    # On this particular problem, it turns out to be easier to just use Dijkstra's (heuristic h(n)=0) than compute the manhattan distance
    path = A_Star(elevGraph,start,end)
    # We subtract the starting point from the path-length
    return len(path)-1

def Part2(data):
    elev, start, end = parseData(data)
    elevGraph = neighbors(elev)
    # We essentially just add a node connected to all possible starts
    elevGraph[(-1,-1)] = {k for k,v in elev.items() if v=='a'}
    # On this particular problem, it turns out to be easier to just use Dijkstra's (heuristic h(n)=0) than compute the manhattan distance
    path = A_Star(elevGraph,(-1,-1),end)
    # We subtract the starting point and the added node from the path-length
    return len(path)-2
from collections import deque

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

def BFS_Path(graph,start,end):
    nodes = deque([start])
    comeFrom = dict()
    
    while len(nodes) > 0:
        n = nodes.popleft()
        if n == end:
            path = []
            node = end
            while node != start:
                path.append(node)
                node = comeFrom[node]
            path.append(start)
            return path

        for newNode in graph[n]:
            if newNode not in comeFrom.keys():
                comeFrom[newNode] = n
                nodes.append(newNode)
    return []

        



def parseData(data):
    locDict = {(ix,iy):i for ix, row in enumerate(data) for iy, i in enumerate(row)}
    start = [k for k,v in locDict.items() if v=='S'][0]
    end = [k for k,v in locDict.items() if v=='E'][0]
    return locDict,start,end

def Part1(data):
    elev, start, end = parseData(data)
    elevGraph = neighbors(elev)
    return len(BFS_Path(elevGraph,start,end))-1

def Part2(data):
    elev, start, end = parseData(data)
    elevGraph = neighbors(elev)
    # We essentially just add a node connected to all possible starts
    elevGraph[(-1,-1)] = {k for k,v in elev.items() if v=='a'}
    # We subtract the starting point and the added node from the path-length
    return len(BFS_Path(elevGraph,(-1,-1),end))-2
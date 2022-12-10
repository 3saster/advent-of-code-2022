DIRECTION = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

def addTuple(a,b):
    return tuple(map(lambda i, j: i + j, a, b))

def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    else: return 0

# Direction to drag tail
def dirTuple(t,h):
    return tuple(map(lambda i, j: sign(i - j), h, t))




# Number of distinct places the tail traveled
def tailTravel(commands,knots):
    knots = [(0,0)]*knots
    visited = set()
    visited.add((0,0))

    for instr in commands:
        [dir,dist] = instr.split(' ')
        for _ in range(int(dist)):
            knots[0] = addTuple(knots[0],DIRECTION[dir])
            # Update each knot's position
            for i in range(1,len(knots)):
                if abs(knots[i][0]-knots[i-1][0]) > 1 or abs(knots[i][1]-knots[i-1][1]) > 1:
                    knots[i] = addTuple(knots[i],dirTuple(knots[i],knots[i-1]))
            visited.add(knots[i])
    return len(visited)

def Part1(data):
    return tailTravel(data,2)

def Part2(data):
    return tailTravel(data,10)
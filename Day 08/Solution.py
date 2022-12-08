from math import prod

def treeScore(trees,i,j):
    vis = [0,0,0,0]
    tree = trees[i][j]
    for I in range(i-1,-1,-1): # Up 
        vis[0] += 1
        if tree <= trees[I][j]: break
    for I in range(i+1,len(trees)): # Down
        vis[1] += 1
        if tree <= trees[I][j]: break
    for J in range(j-1,-1,-1): # Left
        vis[2] += 1
        if tree <= trees[i][J]: break
    for J in range(j+1,len(trees[0])): # Right
        vis[3] += 1
        if tree <= trees[i][J]: break
    return prod(vis)

def Part1(data):
    visible = 0

    trees = [[int(h) for h in heights.strip()] for heights in data]
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            tree = trees[i][j]
            try:
                if  max(trees[i][:j]) < tree or \
                    max(trees[i][j+1:]) < tree or \
                    max([trees[I][j] for I in range(i)]) < tree or \
                    max([trees[I][j] for I in range(i+1,len(trees))]) < tree:
                    visible += 1
            except ValueError:
                visible += 1         
    return visible

def Part2(data):
    visible = 0

    trees = [[int(h) for h in heights.strip()] for heights in data]
    treeScore(trees,1,2)
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            if (s := treeScore(trees,i,j)) > visible:
                visible = s
    return visible
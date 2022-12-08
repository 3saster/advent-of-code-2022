fileTree = None

class Node:
    def __init__(self,name,size=0,children = [], parent = None) -> None:
        self.name = name
        self.children = children
        self.parent = parent
        self.size = size

    def __str__(self):
        names = [child.name for child in self.children]
        if self.parent == None:
            return f"{self.size} {self.name}, children:{names}"
        else:
            return f"{self.size} {self.name}, children:{names}, parent:{self.parent.name}"

class Tree:
    def __init__(self,top):
        self.top = top
        self.curNode = top

    def addChild(self,child):
        child.parent = self.curNode
        self.curNode.children = self.curNode.children + [child]
        self.curNode.size += child.size
        while self.curNode.parent != None:
            self.curNode = self.curNode.parent
            self.curNode.size += child.size
        self.curNode = child.parent

    def display(self,node, level=0):
        print("  "*level+"- " + f"{node.name} {node.size}")
        for child in node.children:
            self.display(child,level+1)

def makeTree(data):
    data = [d.strip() for d in data]
    fileTree = Tree(Node("/"))
    for command in data:
        if command[0] == "$":
            instr = command.split(" ")
            if instr[1] == "cd":
                location = instr[2]
                if location == "/":
                    fileTree.curNode = fileTree.top
                elif location == "..":
                    fileTree.curNode = fileTree.curNode.parent
                else:
                    for child in fileTree.curNode.children:
                        if child.name == instr[2]:
                            fileTree.curNode = child
                            break
            # We don't need to do anything particular for ls
        else:
            files = command.split(" ")
            if files[0] == "dir":
                fileTree.addChild(Node(files[1]))
            else:
                fileTree.addChild( Node(files[1], int(files[0])) )
    fileTree.curNode = fileTree.top
    return fileTree
        
def Part1(data):
    fileSize = 0

    global fileTree
    fileTree = makeTree(data)
    row = [fileTree.top]
    while row != []:
        newRow = []
        for dir in row:
            if dir.children != []:
                if dir.size <= 100000:
                    fileSize += dir.size
                newRow += dir.children
        row = newRow
    return fileSize

def Part2(data):
    global fileTree

    needSpace = 30000000 - (70000000 - fileTree.top.size)

    fileSize = fileTree.top.size
    row = [fileTree.top]
    while row != []:
        newRow = []
        for dir in row:
            if dir.children != []:
                if dir.size > needSpace and dir.size < fileSize:
                    fileSize = dir.size
                newRow += dir.children
        row = newRow
    return fileSize
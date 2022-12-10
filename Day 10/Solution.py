def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def Part1(data):
    commands = " ".join(data).split(" ")
    X = 1
    strength = []
    for i,c in enumerate(commands,1):
        if i%40 == 20: # 20,60,100,...
            strength.append(i*X)
        # Since addx is the only nontrivial instruction
        if isint(c):
            X += int(c)
    return sum(strength[:6])

def Part2(data):
    commands = " ".join(data).split(" ")
    X = 1
    TV = ''
    for i,c in enumerate(commands):
        if i%40 == 0:
            TV += '\n\t'

        if X-1 <= (i%40) <= X+1:
            TV += '██'
        else:
            TV += '  '
        # Since addx is the only nontrivial instruction
        if isint(c):
            X += int(c)
    return TV[2:] # main.py already prints a leading tab
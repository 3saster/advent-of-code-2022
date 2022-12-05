def contained(range1,range2):
    [bot1,top1] = [int(n) for n in range1.split('-')]
    [bot2,top2] = [int(n) for n in range2.split('-')]
    if (bot1 <= bot2 and top2 <= top1) or (bot2 <= bot1 and top1 <= top2):
        return True
    return False

def overlap(range1,range2):
    [bot1,top1] = [int(n) for n in range1.split('-')]
    [bot2,top2] = [int(n) for n in range2.split('-')]
    if (bot1 <= bot2 <= top1) or (bot1 <= top2 <= top1) or (bot2 <= bot1 <= top2) or (bot2 <= top1 <= top2):
        return True
    return False

def Part1(data):
    data = [l.strip() for l in data]
    return len([d for d in data if contained(*d.split(','))])

def Part2(data):
    data = [l.strip() for l in data]
    return len([d for d in data if overlap(*d.split(','))])
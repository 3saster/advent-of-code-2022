calories = list()

def Part1(data):
    data = [l.strip() for l in data]
    global calories
    calories = [0]
    for d in data:
        if d == '':
            calories.append(0)
        else:
            calories[-1] += int(d)
    calories.sort()
    return max(calories)

def Part2(data):
    data = [l.strip() for l in data]
    global calories
    return sum(sorted(calories)[-3:])
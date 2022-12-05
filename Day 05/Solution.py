def parseData(data):
    mid = data.index('')
    stackNum = int(data[mid-1][data[mid-1].strip().rfind(' '):])

    # Stacks
    stacks = {i:[] for i in range(1,stackNum+1)}
    for row in range(mid-1):
        for col in range(1,stackNum+1):
            try: box = data[row][4*col-3]
            except IndexError: break # No more further boxes on this row
            if box != ' ':
                stacks[col].append(box)
    # Instructions
    instructs = []
    for row in range(mid+1,len(data)):
        instructs.append([int(s) for s in data[row].split() if s.isdigit()])
    
    return stacks, instructs

def Part1(data):
    stacks, instructs = parseData(data)
    for inst in instructs:
        boxes = stacks[inst[1]][:inst[0]]
        stacks[inst[1]] = stacks[inst[1]][inst[0]:] # Remove boxes
        stacks[inst[2]] = list(reversed(boxes))+stacks[inst[2]] # Add boxes
    tops = [stacks[col][0] for col in sorted(stacks.keys())]
    return ''.join(tops)

def Part2(data):
    stacks, instructs = parseData(data)
    for inst in instructs:
        boxes = stacks[inst[1]][:inst[0]]
        stacks[inst[1]] = stacks[inst[1]][inst[0]:] # Remove boxes
        stacks[inst[2]] = boxes+stacks[inst[2]] # Add boxes
    tops = [stacks[col][0] for col in sorted(stacks.keys())]
    return ''.join(tops)
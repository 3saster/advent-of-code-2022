from functools import cmp_to_key
from enum import Enum

class Truth(Enum):
    TRUE = 1
    EQUAL = 0
    FALSE = -1

# Returns TRUE if a < b, EQUAL if a = b, FALSE otherwise
def leq(a,b):
    if a < b: return Truth.TRUE
    elif a == b: return Truth.EQUAL
    else: return Truth.FALSE

def lessThan(l1,l2):
    if isinstance(l1,int) and isinstance(l2,int): # Both ints
        out = leq(l1,l2)
    elif isinstance(l1,list) and isinstance(l2,list): # Both lists
        if len(l1) == 0 or len(l2) == 0:
            out = lessThan(len(l1),len(l2))
        else:
            vals = [lessThan(l1[i],l2[i]) for i in range(min(len(l1),len(l2)))]
            if not (Truth.TRUE in vals or Truth.FALSE in vals): # All equal
                out = Truth.TRUE if len(l1) < len(l2) else Truth.FALSE if len(l1) > len(l2) else Truth.EQUAL
            else:
                out = next(v for v in vals if v != Truth.EQUAL)
    elif isinstance(l1,int) and isinstance(l2,list): # int + list
        out = lessThan([l1],l2)
    elif isinstance(l1,list) and isinstance(l2,int): # list + int
        out = lessThan(l1,[l2])
    return out

def parseData(data):
    return [eval(d) for d in data if d != '']

def Part1(data):
    lists = parseData(data)
    packets = [(lists[2*i],lists[2*i+1]) for i in range(len(lists)//2)]
    lessThan(*packets[2])
    correct = [i for i,p in enumerate(packets,1) if lessThan(*p) != Truth.FALSE]
    return sum(correct)

def Part2(data):
    packets = parseData(data) + [ [[2]],[[6]] ]
    compare = lambda a,b: -lessThan(a,b).value
    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]])+1) * (packets.index([[6]])+1)
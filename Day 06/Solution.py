def markerPos(stream,bufSize):
    for i in range(bufSize,len(stream)):
        if len(set(stream[i-bufSize:i])) == bufSize:
            return i
    return -1

def Part1(data):
    return markerPos(data[0],4)

def Part2(data):
    return markerPos(data[0],14)
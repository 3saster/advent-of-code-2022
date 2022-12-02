SCOREVALS = {'win':6,'tie':3,'lose':0}

RPS_GAME = {'rock'    :{'win':'scissors','lose':'paper'   ,'val':1}, \
            'paper'   :{'win':'rock'    ,'lose':'scissors','val':2}, \
            'scissors':{'win':'paper'   ,'lose':'rock'    ,'val':3}  \
}

def matchScore(opp, you):
    if   RPS_GAME[you]['win']  == opp: return SCOREVALS['win']
    elif RPS_GAME[you]['lose'] == opp: return SCOREVALS['lose']
    else:                              return SCOREVALS['tie']

def Part1(data):
    playDict = {'A':'rock','B':'paper','C':'scissors','X':'rock','Y':'paper','Z':'scissors'}
    score = 0
    for game in data:
        [opp,you] = [playDict[hand] for hand in game.split(' ')]
        score += matchScore(opp,you) + RPS_GAME[you]['val']
    return score

def Part2(data):
    playDict = {'A':'rock','B':'paper','C':'scissors'}
    cheatDict = {'X':'lose','Y':'tie','Z':'win'}
    score = 0
    for game in data:
        [opp,res] = [playDict[game[0]], cheatDict[game[-1]]]
        # Pick appropriate hand
        if   res == 'win':  you = RPS_GAME[opp]['lose']
        elif res == 'tie':  you = opp
        elif res == 'lose': you = RPS_GAME[opp]['win']

        score += SCOREVALS[res] + RPS_GAME[you]['val']
    return score
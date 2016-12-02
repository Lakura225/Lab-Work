import random


def game(ra, rb):
    probA = ra / (ra + rb)
    scoreA = 0
    scoreB = 0
    #random.seed(57)
    while True:
        if scoreA >= 11 and scoreA - scoreB >= 2:
            return scoreA, scoreB
            break
        elif scoreB >= 11 and scoreB - scoreA >= 2:
            return scoreA, scoreB
            break
        else:
            rng = random.random()
            if rng < probA:
                scoreA += 1
            else:
                scoreB += 1

def winProbability(ra, rb, n):
    for i in range(n):
        game(ra,rb)
        
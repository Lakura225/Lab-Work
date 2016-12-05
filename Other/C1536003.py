import random


def game(ra, rb):
    probA = ra / (ra + rb)
    scoreA = 0
    scoreB = 0
    # random.seed(57)
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
    Awins = 0
    for i in range(n):
        probA = ra / (ra + rb)
        scoreA = 0
        scoreB = 0
        # random.seed(57)
        for f in range(n):
            if scoreA >= 11 and scoreA - scoreB >= 2:
                Awins += 1
                scoreA = 0
                scoreB = 0
            else:
                rng = random.random()
                if rng < probA:
                    scoreA += 1
                else:
                    scoreB += 1
    prob = Awins / n
    print("{0:.2f}".format(prob))

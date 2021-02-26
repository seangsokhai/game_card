
score = []
money = []
name = []

def winner():
    increase = -1
    for i in score[:-1]:
        increase = increase + 1
        if score[-1] > i:
            mk = money[increase] - 1
            money[increase] = mk
            mm = money[-1] + 1
            money[-1] = mm
        elif score[-1] < i:
            mk = money[increase] + 1
            money[increase] = mk
            mm = money[-1] - 1
            money[-1] = mm
    print(name[0], "score:", score[0], ",", "total money:", money[0])
    print(name[1], "score:", score[1], ",", "total money:", money[1])

    print(name[2], "score:", score[2], ",", "total money:", money[2])
    print(name[3], "score:", score[3], ",", "total money:", money[3])

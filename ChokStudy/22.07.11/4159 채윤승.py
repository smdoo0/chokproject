while True:
    num = int(input())
    if num == 0:
        break
    gs = []
    for i in range(num):
        station = int(input())
        gs.append(station)

    gs.sort()
    fuel =0
    distance = 0
    fin = 0

    for i in range(len(gs)):
        if fuel + distance >= gs[i]:
            distance = gs[i]
            fuel = 200
            if distance >= 1322:
                fin = 1

    if fin == 1:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
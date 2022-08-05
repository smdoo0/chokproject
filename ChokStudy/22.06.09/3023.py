import copy

r, c = map(int, input().split())
card = []
card1 = []                            #좌우대칭
card2 = []                            #상하대칭
for i in range(r):
    card.append([])
    pat = input()
    for j in range(c):
        card[i].append(pat[j])

card1 = copy.deepcopy(card)

for i in range(r):
    for j in range(1, c + 1):
        card1[i].append(card[i][-j])

card2 = copy.deepcopy(card1)

for i in range(1, r + 1):
    card2.append(card1[-i])

a, b = map(int, input().split())

if card2[a - 1][b - 1] == '#':
    card2[a - 1][b - 1] = '.'
else:
    card2[a - 1][b - 1] = '#'

for i in range(r*2):
    for j in range(c*2):
        print(card2[i][j], end = '')
    print('')
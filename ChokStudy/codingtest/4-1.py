n = int(input())
result = [1, 1]

move = list(map(str, input().split()))

for i in move:
    if i == 'R':
        if result[1] < n:
            result[1] += 1
    elif i == 'L':
        if result[1] > 1:
            result[1] -= 1
    elif i == 'U':
        if result[0] > 1:
            result[0] -= 1
    elif i == 'D':
        if result[0] < n:
            result[0] += 1

for i in result: print(i, end = ' ')
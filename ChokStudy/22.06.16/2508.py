T = int(input())

for _ in range(T):
    input()

    box = []
    count = 0
    r, c = map(int, input().split())

    for _ in range(r):
        box.append(input())

    for i in range(r):
        for j in range(c-2):
            if box[i][j] == '>' and box[i][j+1] == 'o' and box[i][j+2] == '<':
                count += 1

    for i in range(r-2):
        for j in range(c):
            if box[i][j] == 'v' and box[i+1][j] == 'o' and box[i+2][j] == '^':
                count += 1

    print(count)
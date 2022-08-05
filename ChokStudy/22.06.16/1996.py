import copy

N = int(input())
m = []
for i in range(N):
        m.append([])
        pat = input()
        for j in range(N):
            m[i].append(pat[j])
newmap = copy.deepcopy(m)                   #맵 복사(출력할 맵)

for y in range(N):
    for x in range(N):
        if newmap[y][x]=='.':            #원래 맵과 출력할 맵의 기존에"."이었던 부분을 숫자 0으로 바꿈
            newmap[y][x] = int(0)
            m[y][x] = int(0)
        else:
            newmap[y][x] = int(newmap[y][x])     #출력할 맵의 기존에 숫자였던 부분을 int형으로 바꿈
            m[y][x] = int(m[y][x])               #원래 맵의 숫자부분을 int형으로 바꿈

for i in range(N):
    m[i].insert(0, 0)
    m[i].append(0)
m.insert(0, [0 for i in range(N+2)])
m.append([0 for i in range(N+2)])
                                            #원래 입력받은 맵 테두리에 0을 추가.(원래 맵의 범위는 1~N+1까지임)
                                            #ex) 0000000
                                            #    0100000
                                            #    0003000
                                            #    0000000
                                            #    0040000
                                            #    0000900
                                            #    0000000

for y in range(1, N+1):
    for x in range(1, N+1):
        if m[y][x] == 0:                      #원래 맵의 .부분
            newmap[y-1][x-1] = m[y-1][x-1] + m[y-1][x] + m[y-1][x+1] + m[y][x-1] + m[y][x+1] + m[y+1][x-1] + m[y+1][x] + m[y+1][x+1]
            #.과 접하는 8개의 숫자를 모두 더해서 출력할 맵의 해당 자리에 더해줌.
            if newmap[y-1][x-1] > 9:
                newmap[y-1][x-1] = 'M'       
        else:
            newmap[y-1][x-1] = '*'

for y in range(N):
    for x in range(N):
        print(newmap[y][x], end = '')
    print('')
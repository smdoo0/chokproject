n = int(input())          #사람의 수

w_h = []                 #몸무게_키를 저장할 리스트

for i in range(n) :
    w_h.append([])
    w, h = map(int, input().split())
    w_h[i].append(w)
    w_h[i].append(h)

ranking = []         #순위를 저장할 리스트

for i in range(n) :                                # i번째 사람이 j번째 사람보다 덩치등수가 낮을때 r에 1을 더해준다.
    r = 1                                             #덩치등수
    for j in range(n) :
        if i != j :
            if w_h[i][0] < w_h[j][0] and w_h[i][1] < w_h[j][1]:
                    r += 1
    ranking.append(r)

for i in ranking :
    print(i, end = ' ')

#55 185     2랑 비교불가, 3보다 작음, 4랑 비교불가, 5보다 큼 ->2등
#60 183     1이랑 비교불가, 3이랑 비교불가, 4랑 비교불가, 5보다 큼 ->1등
#57 186     1보다 큼, 2랑 비교불가, 4랑 비교불가, 5보다 큼 -> 1등
#60 175     1이랑 비교불가, 2랑 비교불가, 3이랑 비교불가, 5보다 큼 ->1등
#46 155     5등
import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = 1         #방문한 지점 0 -> 1
    for i in g[start]:
        if visited[i] == 0:    #현재 위치에서 i번째로 연결된 국가가 한번도 방문하지 않았던 국가라면
            dfs(i)             #그 국가로 이동
            cnt += 1           #탑승한 비행기의 종류 +1

t = int(input())        #테스트 케이스 수

for _ in range(t):
    n, m = map(int, input().split()) #n 은 국가의 수(노드의 수), m은 비행기의 종류(간선의 수)
    g = [[] for i in range(n+1)]
    
#                                    이중리스트 속 숫자는 n번째 국가와 직접 연결된 국가를 의미.
#그래프의 인덱스 값은 서로다른 국가이다. ex)     [[2, 3], [1, 3], [1, 2]]
#                                         -> 첫번째 국가는 2번, 3번국가와 직접 연결되어 있음

    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    
    cnt = 0
    visited = [0]*(n+1) #방문한 국가는 1로 바꿈
    air = []          #탑승한 비행기의 수

    for i in range(n):
        dfs(i)
        if cnt:
            air.append(cnt)
    
    print(min(air))
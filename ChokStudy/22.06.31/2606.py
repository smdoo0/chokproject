#dfs방식. 깊이 우선탐색
#   1 -> 2 -> (1), 3, (5) -> 3 -> (2)   /   -> 5 -> (1), (2), 6 -> (5)
#  2번컴퓨터에서 가장 깊은 곳까지 탐색           5번컴퓨터에서 가장 깊은 곳까지 탐색
n = int(input())          #컴퓨터의 수(노드의 수)
m = int(input())     #연결되어있는 컴퓨터 쌍의 수(간선의 수)
g = [[] for _ in range(n+1)]        #컴퓨터가 1번부터 있으므로(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

cnt = 0
visited = [0]*(n+1) #[1, 1, 1, 0, 1, 1, 0]

def dfs(start):
    global cnt
    visited[start] = 1         #방문한 지점 0 -> 1
    for i in g[start]:
        if visited[i] == 0:   #현재 위치와 연결된 컴퓨터가 방문하지 않았던 컴퓨터라면
            dfs(i)             #그 컴퓨터로 이동
            cnt += 1

dfs(1)              #1번 컴퓨터에 바이러스가 걸렸을 때
print(cnt)
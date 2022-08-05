#bfs방식. 첫 감염 컴퓨터(1)와 연결된 컴퓨터 감염(2, 5) -> 2와 연결된 컴퓨터 감염(3), 5와 연결된 컴퓨터 감염(6)
#         -> 3과 연결된 컴퓨터 감염(2, 이미 감염된 컴퓨터는 if문에 걸려서 안돌아감) -> 6과 연결된 컴퓨터 감염(5, 이미감염)
#         -> 더이상 queue에 아무것도 존재하지 않으므로 while문 탈출

n = int(input())          #컴퓨터의 수(노드의 수)
m = int(input())     #연결되어있는 컴퓨터 쌍의 수(간선의 수)
g = [[] for _ in range(n+1)]        #컴퓨터가 1번부터 있으므로(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

cnt = 0
visited = [0]*(n+1)

def bfs(start):
    global cnt
    visited[start] = 1         #방문한 지점 0 -> 1
    queue = [start]
    while queue:
        for i in g[queue.pop()]:
            if visited[i] == 0:
                visited[i] = 1
                queue.insert(0, i)   #queue의 0위치에 i 삽입
                cnt += 1

bfs(1)
print(cnt)
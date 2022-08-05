n = int(input())          #컴퓨터의 수(노드의 수)
m = int(input())     #연결되어있는 컴퓨터 쌍의 수(간선의 수)
g = [[] for _ in range(n+1)]        #컴퓨터가 1번부터 있으므로(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

print(g)
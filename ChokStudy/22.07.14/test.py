import sys
input = sys.stdin.readline

t = int(input())        #테스트 케이스 수

for _ in range(t):
    n, m = map(int, input().split()) #n 은 국가의 수(노드의 수), m은 비행기의 종류(간선의 수)
    for _ in range(m):
        a, b = map(int, input().split())
    print(n-1)
import sys
t = int(sys.stdin.readline())
air = []  # 정답 받는 리스트

for i in range(t):
    cnt = 0
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(m):
        a,b = list(map(int, sys.stdin.readline().split()))
    air.append(n-1)
for m in range(len(air)):
    print(air[m])


# ab=[[1,2],[2,3],[1,4]]
# stack= 1 2 (2) 3 (1) (3)
# stack에 없는 숫자 나오는 리스트 있으면 cnt +1 해주고 넣어줌, 중복 없애도 되고 있어도 되고
# 어차피 비행기 종류만 셀테니까
# 그리고 stack에 있는 숫자면 continue 해주고 cnt는 그대로
#
# [[2,1],[2,3],[4,3],[4,5]]
#
# stack= 2 1 (2) 3 4 (3) (4) 5
# 1+1+1+1
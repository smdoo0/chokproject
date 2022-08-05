from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
Ti = [list(map(int,input().split())) for _ in range(n)]
Temp = []
result = []
for i in range(n):
    Temp.append(Ti[i][0])
    del Ti[i][0]
    counts = Counter(Ti[i])
    if int(counts.most_common(1)[0][1]) > int(Temp[i]/2):
        print(counts.most_common(1)[0][0])
    else:
        print("SYJKGW")

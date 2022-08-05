from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
Temp = []
result = []
for i in range(n):
    Ti = list(map(int,input().split()))
    Temp.append(Ti[0])
    del Ti[0]
    counts = Counter(Ti)
    if int(counts.most_common(1)[0][1]) > int(Temp[i]/2):
        print(counts.most_common(1)[0][0])
    else:
        print("SYJKGW")
    Ti = []
N = int(input())
stu = []
for i in range(N):
    stu_inf = list(map(int, input().split()))
    stu.append(stu_inf)
stu.sort(key=lambda  x:x[2],reverse=True)#점수를 기준으로 소트
bronze =[[0,0,0]]
y = 2
while True:
    if stu[0][0] == stu[1][0] ==stu[y][0]:
        y += 1
    else:
        bronze[0] = stu[y]
        break

print(stu[0][0], stu[0][1])
print(stu[1][0], stu[1][1])
print(bronze[0][0], bronze[0][1])
a = input().split('-')
num = []

for i in a:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)
    num.append(sum)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
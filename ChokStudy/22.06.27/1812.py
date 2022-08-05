num = int(input())
list=[]
a=0
fin =[]

for i in range(num):
    can = int(input())
    list.append(can)

for i in range(num):
    if i % 2 == 0:
        a += list[i]

    else:
        a -= list[i]

fin.append(a//2)

for i in range(num-1):
    fin.append(list[i]-fin[i])

for i in fin:
    print(i)
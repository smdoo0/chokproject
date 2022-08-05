num = int(input())
box = list(map(int, input().split()))

inbox = [1] * num
for i in range(1, num):
    for j in range (i):
        if box[j]<box[i]:
            if inbox[i] < inbox[j]+1:
                inbox[i] = inbox[j]+1
print(max(inbox))
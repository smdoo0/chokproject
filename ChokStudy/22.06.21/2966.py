N = int(input())
A = ['A','B','C']
B = ['B', 'A', 'B', 'C']
G = ['C', 'C', 'A', 'A', 'B', 'B']
answer = input()
a,b,g = 0,0,0
for i in range(N):
    if answer[i] == A[i%3]:
        a += 1
    elif answer[i] == B[i%4]:
        b += 1
    elif answer[i] == G[i%6]:
        g += 1
print(max(a,b,g))
if max(a,b,g) == a:
    print('Adrian')
if max(a,b,g) == b:
    print('Bruno')
if max(a,b,g) == g:
    print('Goran')
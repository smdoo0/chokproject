n=int(input())
num=list(map(int,input().split())) # 5 12 7 10 9 1 2 3 11
num.sort() # 1 2 3 5 7 9 10 11 12
x=int(input())
cnt=0 # 합이 x인 쌍의 개수
i=0 # 처음 포인터를 조절
j=n-1 # 끝 포인터를 조절

while 1:
    start = num[i]  # 처음 포인터
    end = num[j]  # 끝 포인터

    if start==end:
        break

    if start+end==x:
        cnt+=1
        if j - i == 1:  # 예시로 1 2 3 4 5 6 7 9 10 11 이럴 때, 중간의 합이 x 일 때도 생각
            break       # 이걸 빼먹으면 안됐었다...
        i+=1
        j-=1
    elif start+end>x: # end를 줄여가야 됨
        j-=1
    elif start+end<x: # start를 늘려가야 됨
        i+=1

print(cnt)

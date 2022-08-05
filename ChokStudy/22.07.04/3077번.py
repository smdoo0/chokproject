n=int(input())
right=list(input().split()) # 올바른 정답
hyun=list(input().split()) # 현우가 작성한 답
cnt=0

for i in range(n):
    for j in range(n):
        if right[i]==hyun[j]:
            hyun[j]=i
    right[i]=i

for d in range(n):
    for k in range(1,n-d):
        start=hyun[d]
        end=hyun[d+k]
        if start<end:
            cnt+=1

print("{0}/{1}".format(cnt,n*(n-1)//2))

# 1 2 3 4 5 이렇게 애들 이름을 다 순서로 바꾸자
# 3 5 2 4 1 이렇게 하고 크기 비교를 해 나가면 될 듯!
# start 포인터와 end 포인터를 만들고 end 포인터를 뒤로 보내면서 비교하기
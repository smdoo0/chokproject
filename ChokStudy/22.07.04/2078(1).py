a,b=tuple(map(int,input().split(' ')))
l=0
r=0

#a, b 중 큰 수를 작은 수로 나눈 몫은 이전에 같은방향으로 연속으로 움직인 횟수이다.
#ex) 시작 노드가 (a, b)이고 왼쪽으로 3번연속 이동한다면  (a, b) -> (a+b, b) -> (a+2b, b) -> (a+3b, b)
#따라서 큰 수를 작은 수로 나눈 몫은 한쪽 방향으로 연속해서 이동한 횟수이고 나머지는 반복이 시작되는 곳의 수이다.

while a>1 and b>1:           #둘 중 하나가 1이되면 종료
    if a>b:
        l+=a//b              #왼쪽 값이 더 큰 경우 마지막으로 이동한 방향은 왼쪽. 왼쪽으로 a//b만큼 연속으로 이동함
        a%=b                 #연속으로 이동하기 시작하는 부분
    else:
        r+=b//a
        b%=a

l += a-1
r += b-1

#반복문이 종료됐을 때 (x, 1) or (1, x)인 상태이므로 1인 쪽은 아무것도 더해주지 않고, x인 쪽은 x-1만큼 더해준다.

print(' '.join(map(str,[l,r])))
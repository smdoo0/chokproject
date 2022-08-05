S, K = map(int, input().split())     #S = 합, K = 정수 개수

K_list = [1 for i in range(K)]      # K개의 정수를 저장할 리스트      
x = 0                           # 이중 break를 위한 변수

while True :

    for i in range(K) :
        if sum(K_list) < S :        # K개의 정수의 합이 S보다 작으면
            K_list[i] += 1                  # 각 요소에 1씩 더해줌
        else :                      # K개의 정수의 합이 S가 되면
            x = 1
            break
    
    if x == 1 :
        break

result = 1
for i in K_list :
    result *= i

print(result)
#큰 수의 법칙

n, m, k = map(int, input().split())

# n : 배열의 크기, m : 더할 횟수, k : 같은 인덱스의 수가 연속해서 더해질 수 있는 횟수

n_list = list(map(int, input().split()))
n_list.sort()

#배열 입력, 오름차순 정렬

result = 0
rp = 0

#result : 출력할 결과값, rp : 반복횟수 저장할 변수

for i in range(m) :
    if rp < k :
        result += n_list[-1]
        rp += 1
    else :
        result += n_list[-2]
        rp = 0

#반복횟수가 k보다 작을 때 가장 큰 수를 결과에 더해주고 반복횟수를 늘린다.
#반복횟수가 k가 되면 그 다음 큰 수 를 결과에 더해주고 반복횟수를 초기화한다.

print(result)
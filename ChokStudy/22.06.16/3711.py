N = int(input())          #테스트 케이스 수

for i in range(N):
    G = int(input())        #학생 수
    num = [int(input()) for _ in range(G)]                  #학번 저장할 리스트
    
    m = 1                    #학번을 1부터 나눠가면서 나머지가 다 다를 때 까지 반복할거임

    while True :
        a = [x % m for x in num]             #학번을 m으로 나눈 나머지를 리스트에 저장
        if len(a) == len(set(a)) :           #나머지가 모두 다를 때 (집합으로 만들었을 때 같은 값이 존재하면 길이가 줄어듦)
            print(m)
            break
        else :                               #나머지가 같은 학번이 있을 때
            m += 1
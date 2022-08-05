sum = 0            #점수의 합을 저장할 변수

for i in range(5):
    score = int(input())           #점수가 입력됨
    if score < 40 :                #점수가 40 미만이면 sum에 40 더해줌(논산훈련소식 보충수업)
        sum += 40
    else :                         #점수가 40 이상이면 그대로 sum에 더해줌
        sum += score

avg = int(sum / 5)

print(avg)                         #점수의 합에 학생의 수 5를 나눠서 평균 출력
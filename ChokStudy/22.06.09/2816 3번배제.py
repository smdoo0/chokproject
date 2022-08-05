n = int(input())
c_list = []

for i in range(n):
    c = input()
    c_list.append(c)                 #채널 리스트

result = ''                          #출력할 결과
point = 0                            #화살표 위치

while c_list[0] != 'KBS1':
    if c_list[point] != 'KBS1':            #화살표가 가리키는 위치가 KBS1이 아닐 때 1을 실행
        point += 1
        result += '1'
    else:                                  #화살표가 가리키는 위치가 KBS1일때 4를 실행
        c_list[point - 1], c_list[point] = c_list[point], c_list[point - 1]
        point -= 1
        result += '4'

while c_list[1] != 'KBS2':
    if c_list.index('KBS2') > point:                #KBS2가 화살표보다 아래에 있을 때 1을 실행
        point += 1
        result += '1'
    elif c_list.index('KBS2') > point:              #KBS2가 화살표보다 위에 있을 때 2를 실행
        point -= 1
        result += '2'
    else:                                           #화살표가 가리키는 위치가 KBS2일 때 4를 실행
        c_list[point - 1], c_list[point] = c_list[point], c_list[point - 1]
        point -= 1
        result += '4'

print(result)
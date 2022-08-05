n = int(input())      #단어의 개수
words = [list(map(str, input())) for _ in range(n)]      #단어 저장(이중리스트 사용)
count = 0                                #첫번째 단어와 비슷한 단어 카운트로 개수 세기

for i in range(1, n) :
    std = words[0][:]                           #기준이 되는 첫번째 단어 복사(초기화용)
    test = words[i][:]                         #비교할 단어 복사
    if len(std) == len(words[i]) :          #기준 단어와 문자 수가 같을 때
        for j in range(len(std)) :          #std에 있는 문자가 i번째 단어에 존재하면 그 문자를 0으로 만듦
            for k in range(len(test)) :
                if std[j] == test[k] :
                    std[j] = 0
                    test[k] = 0
        while std.count(0) != 0 :
            std.remove(0)
        if len(std) < 2 :                     #문자가 하나이하로 남는다면
            count += 1                             #비슷한 단어. 개수 세주기.
    elif len(std) - len(test) == 1 :    #기준 단어보다 문자 수가 한 개 적을 때
        for j in range(len(std)) :          #std에 있는 문자가 i번째 단어에 존재하면 그 문자를 0으로 만듦
            for k in range(len(test)) :
                if std[j] == test[k] :
                    std[j] = 0
                    test[k] = 0
        while std.count(0) != 0 :
            std.remove(0)
        if len(std) == 1 :                     #문자가 하나만 남는다면
            count += 1                             #비슷한 단어. 개수 세주기.
    elif len(test) - len(std) == 1 :    #기준 단어보다 문자 수가 한 개 많을 때
        for j in range(len(std)) :          #std에 있는 문자가 i번째 단어에 존재하면 그 문자를 0으로 만듦
            for k in range(len(test)) :
                if std[j] == test[k] :
                    std[j] = 0
                    test[k] = 0
        while std.count(0) != 0 :
            std.remove(0)
        if len(std) == 0 :                     #문자가 없어지면
            count += 1                             #비슷한 단어. 개수 세주기.

print(count)
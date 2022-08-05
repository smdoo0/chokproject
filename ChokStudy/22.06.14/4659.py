import re

while True:
    test = input()
    if test == 'end' :
        break
    
    p1 = re.compile('[aeiou]')                    #모음 컴파일
    m1 = p1.search(test)

    p2_1 = re.compile('[aeiou]{3,}')              #모음이 3번 이상 반복되는 문자열 컴파일
    m2_1 = p2_1.search(test)
    p2_2 = re.compile('[bcdfghjklmnpqrstvwxyz]{3,}')  #자음이 3번 이상 반복되는 문자열 컴파일
    m2_2 = p2_2.search(test)

    p3 = re.compile(r'([a-z])\1')                     #같은 문자가 2번이상 반복되는 문자열 컴파일
    m3 = p3.findall(test)

    if m1 == None:                                #p1을 search했을 때 None이면 모음이 하나도 없다는 뜻이다. 1번조건에 부합하지 않는다.
        print("<%s> is not acceptable." % test)
    elif m2_1 != None or m2_2 != None:                              #p2_1과 p2_2를 search했을 때 None이 아니면 자음 또는 모음이 3번이상 반복되는 부분이 있다는 뜻이다. 2번조건에 부합하지 않는다.
        print("<%s> is not acceptable." % test)
    elif set(m3) | {'e', 'o'} != {'e', 'o'} :               #e, o 외의 다른 문자가 2번 이상 반복됬을 때. 3번조건에 부합하지 않는다.
        print("<%s> is not acceptable." % test)
    else:
        print("<%s> is acceptable." % test)
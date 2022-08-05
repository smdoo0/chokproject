n = int(input())       #구매 의향이 있는 사람의 수 n

m_d = []               #지불할 돈_배송비 저장할 리스트

profit = 0

for i in range(n):
    m_d.append([])
    a, b = input().split()
    a, b = int(a), int(b)
    m_d[i].append(a)
    m_d[i].append(b)

price = 0              #책정가격
profit = 0             #그에 따른 이익
p_p = []               #책정 가격과 그에 따른 이익을 저장할 리스트
profit_list = []       #이익만 저장할 리스트

for i in range(n):
    p_p.append([])
    price = m_d[i][0]            #첫번째 사람부터 제시한 금액을 가격으로 책정했을 때
    for j in range(n):
        if m_d[j][0] >= price:
            if price - m_d[j][1] > 0:        #책정된 가격이 배송비보다 비쌀때(이익이 있을때)
                profit += (price - m_d[j][1])
            else:
                pass
        else:
            pass
    p_p[i].append(price)
    p_p[i].append(profit)
    profit_list.append(p_p[i][1])
    profit = 0

profit_list.sort()                #이익을 오름차순으로 정렬
max = []                          #최대 이익을 내는 가격이 여러개일 때 그 가격을 저장할 리스트

for i in range(n):
    if profit_list[-1] == 0:                   #이익이 없을때
        print(0)
        break
    elif len(profit_list) != len(set(profit_list)):             #최대 이익을 내는 가격이 여러개일 때
        for j in range(n):
            if p_p[j][1] == profit_list[-1]:
                max.append(p_p[j][0])
        max.sort()
        print(max[0])
    elif p_p[i][1] == profit_list[-1]:
        print(p_p[i][0])
        break
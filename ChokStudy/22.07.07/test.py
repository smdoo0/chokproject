import re

alp = re.compile('[A-Z]')        #알파벳 대문자

n = int(input())         #피연산자의 개수

q = input()              #후위표기식
q = [i for i in q]       #입력된 후위표기식을 문자단위로 리스트에 담음
num = [int(input()) for _ in range(n)]   #피연산자에 대응하는 값

temp1 = []         #입력된 식에서 알파벳만 순서대로 뽑아서 저장할 리스트
temp2 = []         #알파벳에 해당하는 값을 대입할 리스트

for i in range(len(q)):
    m = alp.match(q[i])
    if m:                        #q안의 피연산자 순서대로 저장하기(temp1에 알파벳만 저장)
        temp1.append(q[i])

s_temp1 = []
for i in temp1:
    if i not in s_temp1:
        s_temp1.append(i)              #중복된 알파벳 제거하고 저장

for i in range(len(s_temp1)):
    for _ in range(temp1.count(s_temp1[i])):           #temp2에 알파벳에 대응하는 값 저장
        temp2.append(num[i])

for i in range(len(q)):
    m = alp.match(q[i])
    if m:
        q[i] = temp2.pop(0)                 #q의 알파벳에 해당하는 값을 대입

#여기까지가 입력된 후위표현식의 피연산자에 해당 값을 대입하는 과정(ex) ABC*+DE/-   ---->   123*+45/-

print(q)
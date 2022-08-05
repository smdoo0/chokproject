n=int(input()) # 피연산자 개수
back=list(input()) # 후위 표기식
o=[input() for _ in range(n)] # 피연산자

i,j=0,0 # i는 back의 요소를, j는 o의 요소를 꺼내와서 비교
while i!=len(back): # 후위 표기식의 알파벳을 피연산자 숫자로 바꿔주는 작업
    if back[i].isalpha()==True:
        back[i]=o[j]
        i+=1
        j+=1
        if j==len(o): # j가 o의 요소 개수보다 크면 o의 범위를 벗어나게 됨
            j-=1 # 그래서 j에 1을 빼줌 으로써 앞에서 j+=1을 해도 문제 없게 함
    else :
        i+=1

num=[]
for k in range(len(back)):
    if back[k].isdigit()==True: # 피연산자라면
        num.append(int(back[k]))
    else: # 연산자라면
        np1 = num.pop()
        np2 = num.pop()
        if back[k]=='+':
            num.append(np1+np2)
        elif back[k]=='-':
            num.append(np2-np1)
        elif back[k]=='*':
            num.append(np1*np2)
        elif back[k] == '/':
            num.append(np2/np1)
print("{:.2f}".format(*num))

# 123*+45/-
# ((1(23)*)+(45)/)-
# (1+(2*3)-(4/5))
# 1+(2*3)-(4/5)
# 1+6-0.8

# 1
# 1 2
# 1 2 3 <- *
# 1 6 <- +
# 7
# 7 4
# 7 4 5 <- /
# 7 0.8 <- -
# 6.2
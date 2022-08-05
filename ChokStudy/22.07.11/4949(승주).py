import sys

def pair(stack):           #짝맞추기 함수)]
    c_stack = stack[:]
    if len(stack) > 1:           #여는괄호 없이 닫는괄호만 나왔을 경우 제외
        close = c_stack.pop()
        open = c_stack.pop()
        if open == '(' and close == ')':
            for _ in range(2): stack.pop()        #짝이 맞는다면 해당 괄호 쌍 제거
        elif open == '[' and close == ']':
            for _ in range(2): stack.pop()

#stack에는 괄호만 저장된다.
#짝을 이루는 상태라면 stack의 마지막 요소가 닫는괄호고 마지막에서 두번째 요소가 여는괄호일 것이다.

while True:
    data = sys.stdin.readline().rstrip()          #input 보다 빠르게 입력받는 방법
    
    if data == '.':      #반복분 탈출 조건
        break
    
    stack = []
    
    #문자열에 여는괄호가 나오면 stack에 저장. 닫는 괄호가 나오면 stack에 저장하고 짝맞추기 함수 호출
    
    for i in data:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            stack.append(i)
            pair(stack)
        elif i == ']':
            stack.append(i)
            pair(stack)
    
    #모든 짝이 맞아서 stack에 아무 요소가 없다면 yes

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
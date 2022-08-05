while 1:
    word=input()
    stack=[]

    if word=="." :
        break
    for i in word:
        if i=='(' or i=='[':
            stack.append(i) # 왼쪽 소괄호와 대괄호는 오른쪽이 올 걸 대비해서 받아주기만 한다
        elif i==')':
            if len(stack)!=0 and stack[-1]=='(': # ( 랑 짝이 맞춰졌을 때
                stack.pop()
            else:
                stack.append(')')
                break
        elif i==']':
            if len(stack) != 0 and stack[-1] == '[': # [ 랑 짝이 맞춰졌을 때
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack)==0: # 공백으로만 이루어져 있어도 stack은 0이니까 yes
        print("yes")
    else:
        print("no")
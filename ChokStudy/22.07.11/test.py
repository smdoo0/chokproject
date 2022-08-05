import sys

def pair(s):
    global stack
    if len(stack) > 1:
        close = s.pop()
        open = s.pop()
        print(open)
        print(close)
        print(stack)

while True:
    data = sys.stdin.readline().rstrip()          #input 보다 빠르게 입력받는 방법
    stack = []
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
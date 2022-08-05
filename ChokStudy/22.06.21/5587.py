n = int(input())        #카드의 개수. 카드는 1~2n까지 한장씩 있음

sg = [int(input()) for _ in range(1, n+1)]                  #상근이의 카드 n장을 입력받음.
gs = [int(num) for num in range(1, 2*n+1) if num not in sg]      #근상이의 카드. 1~2n중에 상근이가 없는 숫자 저장.

sg.sort()
gs.sort()

card = 0                             #놓여진 카드. 아무것도 안놓여진 상태는 0

while len(sg) != 0 and len(gs) != 0 :              #둘중 한명이라도 카드를 다 쓰면 종료
    sg_card = len(sg)                       #현재 상근이의 카드개수 저장
    for i in sg :
        if card < i :                       #상근이가 낼 수 있는 가장 작은 숫자가 놓여있는 숫자보다 크다면
            card = i
            sg.remove(i)                   #그 숫자를 카드에 저장하고 리스트에서 제거
            break
    if sg_card == len(sg) :             #for문 이후에 카드개수가 같다면 아무카드도 못낸것.
        card = 0                        #놓여있는 카드는 초기화되고 상대턴으로 넘어감.

    gs_card = len(gs)                       #근상이 턴.
    for i in gs :
        if card < i :
            card = i
            gs.remove(i)
            break
    if gs_card == len(gs) :
        card = 0


sg_score = len(gs)                     #상대방의 남은 카드 개수가 점수가 된다.
gs_score = len(sg)

print(sg_score)
print(gs_score)
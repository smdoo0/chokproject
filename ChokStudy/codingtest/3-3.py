#숫자 카드 게임
n, m = map(int, input().split())
card = []

for _ in range(n):
    card.append(list(map(int, input().split())))

a = []

for i in range(n):
    a.append(min(card[i]))

print(max(a))
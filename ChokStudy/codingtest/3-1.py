n = int(input())    #거슬러줘야되는 돈
coin_type = [500, 100, 50, 10]
coin = 0            #동전의 개수

for i in coin_type :    
    coin += n // i
    n %= i

print(coin)
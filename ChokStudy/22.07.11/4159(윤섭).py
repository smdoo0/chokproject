while True:
    n = int(input())
    if n == 0:
        break
    locate = [int(input()) for _ in range(n)]
    locate.sort(reverse=True)
    temp = []
    for i in range(n-1):
        temp.append(locate[i]-locate[i+1])
    if 1422 - locate[0] > 100:
        print("IMPOSSIBLE")

    elif max(temp) <= 200:
        print("POSSIBLE")
        locate = []
    else:
        print("IMPOSSIBLE")
        locate = []

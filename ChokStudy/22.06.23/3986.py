n = int(input())

count = 0
for i in range(n):
    word = input()
    ab = []
    for j in word:
        if len(ab) == 0:
                ab.append(j)
        else:
            if j == "A":
                if ab[-1] == "B":
                    ab.append(j)
                elif ab[-1] == "A":
                    ab.pop()

            elif j == "B":
                if ab[-1] == "A":
                    ab.append(j)
                elif ab[-1] == "B":
                    ab.pop()

    if len(ab)==0:
        count+=1

print(count)
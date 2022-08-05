k = int(input())
cho = 1
max =1
count = -1

while k > cho:
    cho *= 2

max = cho

while k != 0:
    if k >= cho:
        k -= cho
    cho /= 2
    count += 1

print(max, count)
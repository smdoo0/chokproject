s = input()
s = [int(i) for i in s]
temp = 0

while len(s) > 1:
    if s[0] * s[1] > s[0] + s[1]:
        temp = s.pop(0) * s.pop(0)
        s.insert(0, temp)
    else:
        temp = s.pop(0) + s.pop(0)
        s.insert(0, temp)

print(s[0])
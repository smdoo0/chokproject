import sys
num = int(sys.stdin.readline())
start = 0
save = 0
time = [0]
dtime = []

for _ in range(num):
    music, down = map(int, sys.stdin.readline().split())
    time.append(music)
    dtime.append(down)

for i in range(num):
    while True:
        if dtime[i] > time[i] + save:
            time[i] += 1
            start += 1
        else:
            save = (time[i] + save) - dtime[i]
            break
print(start)
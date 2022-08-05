import sys
n=int(sys.stdin.readline())

queue=[]
for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    # [0],[2,3,2],[0],[0],[0]
    if a[0]: # a[0]가 0이 아닐 때 (거점지)
        queue+=a[1:] # 충전한 선물 -> 큐 쌓기! ex) queue=[3,2]
    else: # a[0]==0 일 때 (아이들)
        if len(queue): # (충전한) 선물이 있을 때
            print(max(queue))
            queue.remove(max(queue))
        else: # (충전한) 선물이 없을 때
            print("-1")


# import sys
# n=int(sys.stdin.readline())
#
# point=[]
# for _ in range(n):
#     a=list(map(int,sys.stdin.readline().split()))
#     point.append(a)
#
# queue=[]
# present=[]
# for i in point:
#     if i[0]!=0:
#         queue=i[1:] # 충전한 선물 -> 큐 쌓기! ex) queue=[3,2]
#     else:
#         if len(queue)==0: # (충전한) 선물이 없을 때
#             present.append(-1)
#         else: # (충전한) 선물이 있을 때
#             idx=queue.index(max(queue))
#             present.append(max(queue))
#             queue.pop(idx)
#
# for j in present:
#     print(j)
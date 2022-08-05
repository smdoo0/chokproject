# 파이썬 문자열에서 숫자만 추출 해보는 방식으로 해볼까..? -> 정규표현식
import re

n=int(input())
word=[input() for _ in range(n)]
num=[] # 종이에서 찾은 숫자
remove_0=[] # 앞에 오는 0을 없앤 숫자 (선행 0를 없앤 숫자)

for i in range(n):
    digit=re.findall("\d+",word[i]) # 문자열 중 숫자만 찾아서 리스트로 만들어줌
    num.append(digit) # 이렇게 하면 num은 2차원 리스트가 됨

num=sum(num,[]) # 2차원 리스트를 1차원 리스트로 만드는 법 : 2차원 리스트 요소들(리스트들)을 다 더한다

for j in num:
    if len(j)>1: # 그냥 0일 경우를 대비
        j.lstrip('0') # lstrip() : 인자로 전달된 문자를 다른 문자가 나올 때 까지 String의 왼쪽에서 제거
    j=int(j) # 이렇게 안하면 오름차순할 때 이상하게 될 수 있음 ex) 231233 43 중 231233이 먼저 옴
    remove_0.append(j)

remove_0.sort() # 비내림차순=오름차순

for k in remove_0:
    print(k)

# for j in range(len(num)):
#     for k in range(len(num[j])):
#         if len(num[j])>1: # 그냥 0 한 개만 있을 경우를 대비
#             if num[j][k]!=0: # 100 이런 경우를 대비
#                 # 앞에 0이 아닌 숫자가 오고 0이 온 경우 ex) 20
#                 continue
#             else:
#                 if k==0:
#                     num.remove(num[j][k])
#                 elif k>0 and k!=len(num[j]):
#                     for m in range()
#                 else: # k==len(num[j])
#                     continue

# 해당 작업시 큐의 인덱스 아웃 문제 고려, front end pop 등등


import sys
from collections import deque
n = int(input())
result = deque()
for x in [ sys.stdin.readline().split() for _ in range(n)]:
    if x[0] == 'push':
        result.append(x[1])
    elif x[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())

    elif x[0] == 'size':
        print(len(result))
    elif x[0] == 'empty':
        if len(result) > 0 : print(0) 
        else : print(1)
    elif x[0] == 'front':
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    elif x[0] == 'back':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])



# import sys
# from collections import deque
# n = int(input())
# result = deque()
# for i in range(n):
#     x = sys.stdin.readline().split()
#     if x[0] == 'push':
#         result.append(int(x[1]))
#     elif x[0] == 'pop':
#         if len(result) == 0:
#             print(-1)
#         else:
#             print(result.popleft())
#     elif x[0] == 'size':
#         print(len(result))
#     elif x[0] == 'empty':
#         if len(result) > 0 : print(0) 
#         else : print(1)
#     elif x[0] == 'front':
#         if len(result) == 0:
#             print(-1)
#         else:
#             print(result[0])
#     elif x[0] == 'back':
#         if len(result) == 0:
#             print(-1)
#         else:
#             print(result[-1])
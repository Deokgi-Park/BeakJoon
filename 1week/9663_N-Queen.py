import sys
sys.setrecursionlimit(100000)
N = int(input())

Qset = [None] * N 
row = [False] * N
crossXY = [False] * (N*2-1)
crossYX = [False] * (N*2-1)
cnt = 0

def putQueen(i):
    global N, cnt    
    for j in range(N):
        if (not row[j] and not crossXY[i+j] and not crossYX[i-j+(N-1)]):
            Qset[i] = j
            if i == (N-1):
                cnt +=1
            else :
                row[j] = crossXY[i+j] = crossYX[i-j+(N-1)] = True
                putQueen(i+1)
                row[j] = crossXY[i+j] = crossYX[i-j+(N-1)] = False

putQueen(0)
print(cnt)
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
graph = []
# 좌표이동 문제 다음과 같이 처리
# dx = [ -1, 1, 0, 0]
# dy = [ 0, 0, -1, 1]
for i in range(N):
    graph.append(list(map(int,input())))

def moving(Y, X):
    global graph
    q = deque()
    q.append([Y,X])
    while q : 
        Y, X = q.popleft()
        if Y==N-1 and X == M-1:
            print(graph[Y][X])
            break

        # 좌표이동 문제 다음과 같이 처리
        #for i in range(4):
        #tmp_X = X + dx[i]
        #tmp_Y = Y + dy[i]
        if X+1 <= (M-1) and graph[Y][X+1] == 1:
                q.append([Y,X+1])
                graph[Y][X+1] = graph[Y][X]+1
        if Y+1 <= (N-1) and graph[Y+1][X] == 1:
                q.append([Y+1,X])
                graph[Y+1][X] = graph[Y][X]+1
        if Y-1 >= 0 and graph[Y-1][X] == 1:
                q.append([Y-1,X])
                graph[Y-1][X] = graph[Y][X]+1
        if X-1 >= 0 and graph[Y][X-1] == 1:
                q.append([Y,X-1])
                graph[Y][X-1] = graph[Y][X]+1
moving(0, 0)
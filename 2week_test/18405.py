from collections import deque
N, K = map(int, input().split())
graph = []
visited = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    visited.append([False] * N)
S, X, Y = map(int, input().split())
# 0 위 1 아래 2 왼 3 오
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

end = []
def bfs(X, Y):
    global graph
    q.append([X, Y])
    second = 0
    while q:
        nowX, nowY = q.popleft()
        if graph[nowX][nowY] != 0 or S == 0:
            end.append([second, graph[nowX][nowY]])
            break
        visited[nowX][nowY] = True
        if graph[nowX][nowY] == 0:
            second += 1
            for i in range(4):
                tmp_X = nowX + dx[i]
                tmp_Y = nowY + dy[i]
                if tmp_X>=0 and tmp_X<N and tmp_Y<N and tmp_Y>=0 and not visited[tmp_X][tmp_Y]:
                    if graph[tmp_X][tmp_Y] != 0:
                        end.append([second, graph[tmp_X][tmp_Y]])
                    elif graph[tmp_X][tmp_Y] == 0 and second <= S-1:
                        q.append([tmp_X,tmp_Y])
bfs(X-1,Y-1)
end.sort()
if end:
    print(end[0][1])
else : 
    print(0)

## 잘못 품..
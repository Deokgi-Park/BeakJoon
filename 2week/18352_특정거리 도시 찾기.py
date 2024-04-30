import sys
from collections import deque

N, E, W, S = map(int, sys.stdin.readline().strip().split())
visited = [False] * (N+1)
dis = [float("inf")] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(E):
    node1, node2 =  map(int, sys.stdin.readline().strip().split())
    graph[node1].append(node2)
    
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    dis[start] = 0 
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i] :
                dis[i] = dis[v] + 1
                q.append(i)
                visited[i] = True

bfs(S)
cnt = 0
for i, v in enumerate(dis):
    if v == W :
        print(i)
        cnt+=1
if cnt == 0:
    print(-1)
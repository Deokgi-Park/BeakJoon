import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
V = {}
visited = [0] * (N+1)
for i in range(N+1):
    V[i] = []
    
for i in range(N-1):
    data1, data2 = map(int,input().split())
    V[data1].append(data2)
    V[data2].append(data1)

def dfs(start, root):
    visited[start] = root
    for i in V[start]:
        if visited[i] == 0 : 
            dfs(i, start)

dfs(1, 1)

for i in range(2,N+1):
    print(visited[i])
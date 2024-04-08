import sys
import heapq

N = int(input())
need = int(input())
graph = [[] for _ in range(N+1)]
weight = [0 for _ in range(N+1)]

for i in range(N):
    E, S, W = map(int, sys.stdin.readline().strip().split())
    graph[E].append([W,S])
    #weight[S] = weight[S]+W
q = []
result = {}
for i in range(1,N):
    if graph[i] == [] :
        heapq.heappush(q, [0,i])
        result[i] = 0

print(graph)
print(result)
print(weight)
while q:
    V = heapq.heappop(q)
    print(q)


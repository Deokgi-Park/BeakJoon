# 4 6
# 1 2 1
# 2 3 2
# 2 4 5
# 4 1 2
# 4 3 6
# 1 3 3



#짧은 간선 찾기, 연결 
import heapq
N, E = map(int, input().split())
graph = []
q = []
status = [0] * (N+1)
for i in range(N+1):
    status[i] = i


for i in range(E):
    graph.append((list(map(int, input().split()))))
result = 0

def MST():
    global result
    for node in graph:
        data = [node[2],node[0],node[1]]
        heapq.heappush(q, data)
    while q:
        nodedata = heapq.heappop(q)
        a = parent_checker(nodedata[1]) 
        b = parent_checker(nodedata[2]) 
        if a != b :
            status[max(a,b)] = min(a,b) 
            result += nodedata[0]

def parent_checker(i):
    if i != status[i] :
        return parent_checker(status[i])
    else :
        return status[i]

MST()
print(result)
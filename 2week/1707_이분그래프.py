import sys
set
N = int(input())
sys.setrecursionlimit(10 ** 6)
#visited -1 : 레드 
# 0 : 미방문 
# 1 : 블루

def dfs(start, graph, visited, status):
    if visited[start] != status:
        result.append(True)
        visited[start] = status*(-1)
        for i in graph[start]:
            if visited[i] == 0:
                dfs(i, graph, visited, status*(-1))
            elif visited[i] != status: 
                result.append(False)

for i in range(N):
    node, edge = map(int, sys.stdin.readline().strip().split())
    result = []
    data = {}
    visited = [0] * (node+1) 
    for i in range(node+1):
        data[i] = []
    
    for i in range(edge):
        nodes = list(map(int, sys.stdin.readline().strip().split()))
        data[nodes[0]].append(nodes[1])
        data[nodes[1]].append(nodes[0])
    
    dfs(1, data, visited, -1)
    for i in range(1, node+1):
        if visited[i] == 0 :
            dfs(i, data, visited, -1)

    if result.count(False) > 0:
        print("NO")
    else:
        print("YES")
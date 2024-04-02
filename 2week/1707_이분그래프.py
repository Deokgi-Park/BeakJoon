N = int(input())


    
def dfs(start, data, visited):
    visited[start] = True
    if not visited[start]:
        for i in data[start]:
            dfs(i)

for i in range(N):
    node, edge = map(int, input().split())
    data = {}
    visited = [False] * (node+1) 
    for i in range(node+1):
        data[i] = []
    
    for i in range(edge):
        nodes = list(map(int, input().split()))
        data[nodes[0]].append(nodes[1])
        data[nodes[1]].append(nodes[0])
    
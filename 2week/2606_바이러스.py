N = int(input())
E = int(input())
data = {}
visited = [False] * (N+1)
for i in range(N+1):
    data[i] = []
for i in range(E):
    pic = list(map(int, input().split()))
    data[pic[0]].append(pic[1])
    data[pic[1]].append(pic[0])


def dfs(start):
    global count
    visited[start] = True
    for i in data[start]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(visited.count(True)-1)
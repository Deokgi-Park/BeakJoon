N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
answer = 0
cnt = 1

def dfs(init, visited, start, total):
    global answer, arr, cnt
    if cnt == len(visited):
        if arr[start][init] != 0:    
            visited[init] = 1
            total += arr[start][init]
        else :
            return
    if 0 not in visited :
        if init == 0 and answer == 0 :
            answer = total 
        if answer > total :
            answer = total
        visited[init] = 0
        return
    for end in range(len(visited)):
        if init == end:
            continue
        if arr[start][end] == 0:
            continue
        if visited[end] == 1:
            continue
        visited[end] = 1
        cnt += 1
        dfs(init, visited, end, total + arr[start][end])
        cnt -= 1
        visited[end] = 0
        

for i in range(N):
    visited = [0] * N 
    dfs(i, visited, i, 0)
print(answer)
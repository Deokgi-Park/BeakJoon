def dfs(start,cost,count):
    global result
    # 횟수가 n-1번이다 -> 모든 도시 다 돌았다.
    # arr[start][0] != 0 마지막 지점에서 1로 돌아가는 길이 있다
    if count == n-1 and arr[start][0] != 0:
    	# 최소값은 비용에다가 돌아가는 비용 더한거랑 비교
        result = min(result,cost+arr[start][0])
        return

    for i in range(n):
        if visited[i] == 0 and arr[start][i] != 0:
            visited[i] = 1
            # 출발지점을 i로
            # 비용에 i로 가는 비용 더해주기
            # 횟수 + 1
            dfs(i,cost+arr[start][i],count+1)
            visited[i] = 0

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 확인을 위한 visited
# 1부터 n까지만 확인하면 되므로
visited = [0] * n

result = int(1e9)

visited[0] = 1
# 시작지점, 비용, 횟수
dfs(0,0,0)
print(result)
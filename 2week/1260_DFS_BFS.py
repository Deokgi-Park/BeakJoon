from collections import deque

N, M, V = map(int, input().split())
# 노드 별 인접 노드 리스트 빈배열 생성, 1번부터 N번 까지의 노드이기 때문에 햇갈리지 않게 0번 배열 빈배열 추가
data = [[] for _ in range(N+1)]
# 인접리스트 노드별로 데이터 넣기
for i in range(M):
    a, b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

# 인접리스트 데이터 정렬
for i in range(N+1):
    data[i].sort()

# 노드 갯수만큼 방문 여부 생성, 0번 배열 빈배열 추가 
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)


# 재귀함수를 통한 구현
def dfs(data,start):
    # 첫 노드 출력
    print(start, end=" ")
    # 방문 처리
    visited_dfs[start] = True
    # 현재 노드 인접 리스트 재귀 호출(스택 쌓기)
    for i in data[start]:
        # 방문여부 체크
        if not visited_dfs[i]:
            # 방문하지 않은 경우 출력하기 위해 재귀 처리
            dfs(data, i)

# 큐를 통한 구현
q = deque()
def bfs(data, start):
    # 큐에 노드 키를 담는다
    q.append(start)
    # 방문 노드를 체크 처리 한다.
    visited_bfs[start] = True
    # 큐가 없을 때까지 while 동작
    while q :
        # 큐에 넣은 노드를 pop 하고 출력
        node = q.popleft()
        print(node, end= " ")

        # 큐에 넣은 인접 노드들을 큐에 쌓는다.
        for v in data[node]:
            # 큐에 넣은 인접 노드들 중 방문된 것을 스킵한다.
            if not visited_bfs[v]:
                # 큐에 노드를 넣는다.
                q.append(v)
                # 큐에 넣은 노드를 방문 처리
                visited_bfs[v] = True
dfs(data,V)
print()
bfs(data,V)
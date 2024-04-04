# 세로 가로 값 입력
N,M = map(int, input().split())
# 나무 변수 선언
tree = []
# 나무 값 입력
for i in range(N):
    tree.append(list(input()))
# 나무 갯수
cnt = 0
# 나무 카운터 동작
def counter(Y):
    global cnt
    # 나무 카운터 정지 조건
    if Y >= N :
        return
    # 나무 카운터
    for X in range(M):
        # 나무 카운터 '-' 일 경우
        if tree[Y][X] == '-':
            if X > 0 and tree[Y][X] == tree[Y][X-1]:
                continue
            cnt += 1
        # 나무 카운터 '|' 일 경우
        if tree[Y][X] == '|':
            if Y > 0 and tree[Y][X] == tree[Y-1][X]:
                continue
            cnt += 1
    # 나무 재귀 호출        
    counter(Y+1)
# 0 부터 시작
counter(0)
# 프린트
print(cnt)

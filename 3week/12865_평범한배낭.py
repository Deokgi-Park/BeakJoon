# 물건 종류, 가방 입력
kind, pack = map(int, input().split())
# 0번 항목 공란화
tool = [[0,0]]
# 가방 공간이 0인 경우와 준비된 물건이 없는 경우를 추가
# 배열의 0번 항목 셋팅으로 +1
dp = [[0] * (pack+1) for _ in range(kind+1) ]

# 물건 입력
for i in range(kind):
    tool.append(list(map(int, input().split())))

# 물건 갯수와, 가방 칸수를 가정해서 각 가방 j 칸일 경우 i 물건을 어떻게 채울 수 있는지 테이블 작성
for i in range(1, kind+1):
    for j in range(1, pack+1):
        if tool[i][0] > j:
           dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-tool[i][0]]+tool[i][1])

print(dp[kind][pack])
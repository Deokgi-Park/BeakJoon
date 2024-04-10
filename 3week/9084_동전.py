def run():
    # 코인 갯수, 현재는 코인 종류만큼 돌릴 것으로 필요 없음
    coinKind = int(input())
    # 코인을 종류 별로 리스트에 담기
    # 해당 리스트는 오름차순으로 되어 있는 정보를 받음...(필수)
    coins = list(map(int, input().split()))
    # 목표치를 선택
    target = int(input())
    # DP 체크용 테이블 생성, 미리 최대치 생성하는 것이 왠만하면 좋은 듯..
    dp = [0] * 10001
    # DP[0]일 때 가능했는 지 여부
    dp[0] = 1
    # 코인 별로 DP 동작 수행
    for coin in coins : 
        # 코인 금액 부터 시작, 
        # 현재 목표금액인 i에서 코인 금액을 뺄 경우 이전에 가능했는지 체크해서 경우의 수 +1 
        for i in range(coin, target+1):
            dp[i] = dp[i-coin]
    # 위 동작 수행 시 target 번째 배열에는 가능한 모든 방법의 cnt 가 생김 
    print(dp[target])

testCase = int(input())

for _ in range(testCase):
    run()

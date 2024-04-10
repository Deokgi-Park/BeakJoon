one = input()
two = input()

dp = [[0] * (len(two)+1) for _ in range(len(one)+1) ]


for i,char1 in enumerate(one,start=1):
    for j,char2 in enumerate(two,start=1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif char1 == char2 :
            dp[i][j] = dp[i-1][j-1]+1
        elif dp[i][j-1] >= dp[i-1][j]:
            dp[i][j] = dp[i][j-1]
        else :
            dp[i][j] = dp[i-1][j]
        if i == len(one) and j == len(two):
            print(dp[i][j])

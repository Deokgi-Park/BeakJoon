n = int(input())
zeroone = [0] * 1000001
zeroone[1] = 1
zeroone[2] = 2
for i in range(3, n+1):
    zeroone[i] = (zeroone[i - 1] + zeroone[i - 2])%15746
print(zeroone[n])


# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2

# for k in range(3,n+1):
#     dp[k] = (dp[k-1]+ dp[k-2])%15746
# print(dp[n])
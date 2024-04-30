round = int(input())
floorData = [0]
for floor in range(round):
    floorData.append(int(input()))
floorData.append(0)
floorData.append(0)
floorData.append(0)
dp = [0] * (10)

dp[round] = 1

#print(dp)
#print(floorData)

point = 0

for i in range(1,round) :
    # elif dp[i+1] == 1:
    #     continue
    # elif sum(dp[i-2:i-1]) == 2:
    #     continue
    if dp[i-1] == 0 and floorData[i] + floorData[i+1] >= floorData[i+1] + floorData[i+2]:
        dp[i] = 1
        dp[i+1] = 1
        i += 2
    elif dp[i-1] == 1 and floorData[i] + floorData[i+1] >= floorData[i+1] + floorData[i+2]:
        dp[i+1] = 1
        dp[i+2] = 1
        i += 2
    elif dp[i-1] != 1:
        dp[i] = 1
        dp[i+2] = 1
        i += 2
for i in range(1, len(floorData)):
    if dp[i] == 1:
        point += floorData[i]
print(point)
print(dp)
N, S = map(int,input().split(' '))
data = list(map(int, input().split(' ')))

cnt = 0
ans = []

def sumdata(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1
    
    for i in range(start, N):
        ans.append(data[i])
        sumdata(i+1)
        ans.pop()

sumdata(0)
print(cnt)
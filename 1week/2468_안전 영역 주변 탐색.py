import copy
# 하... 리커전 오류 날때 아래 참조 최대 리커전(재귀량) 증량
import sys
sys.setrecursionlimit(100000)

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
checker = [[True]*N]*N
max = max([max(x) for x in arr])
maxSaft = 0

def saftChecker(hight, arrdata):
    cnt = 0
    for x, data in enumerate(arrdata):
        for y, org in enumerate(data):
            if hight < org:
                cnt += 1
                run(x, y, arrdata, hight)
    return cnt

def run(x, y, arrdata2, hight):
    # 상하 좌우 체크해서 주변값 및 체커를 0,false로 만들기 및 cnt + 1
    if hight < arrdata2[x][y]:
        arrdata2[x][y] = 0
        if 0<=x-1<len(arrdata2[0]):
            run(x-1,y,arrdata2,hight)
        if 0<=x+1<len(arrdata2[0]):
            run(x+1,y,arrdata2,hight)
        if 0<=y-1<len(arrdata2[0]):    
            run(x,y-1,arrdata2,hight)
        if 0<=y+1<len(arrdata2[0]):    
            run(x,y+1,arrdata2,hight)
    else :
        return

for hight in range(max):
    b = copy.deepcopy(arr)
    if hight == 0 :
        maxSaft = 1
    else :
        cnt = saftChecker(hight, b)
        if maxSaft < cnt:
            maxSaft = cnt
print(maxSaft)
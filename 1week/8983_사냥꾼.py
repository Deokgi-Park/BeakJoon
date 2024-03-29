import sys
M,N,L = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))
pos.sort()
animals = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
count = 0


for x, y in animals:
    # y 사거리를 X좌표에 맞추기 위해 
    # L(사거리) - y 를 해서 동물이 최대 사거리 내인지 체크
    # 최대 사거리 이상의 동물일 경우 미체크
    if L < y :
        continue 
    newMaxL = L-y
    
    # 사수를 이분 탐색 할 것
    start = 0
    end = M-1
    
    while start<=end :
        mid = (start+end) // 2
        min = pos[mid]-newMaxL
        max = pos[mid]+newMaxL
        if min <= x <= max : 
            count += 1
            break
        elif x < max :
            end = mid-1
        else :
            start = mid+1
print(count) 

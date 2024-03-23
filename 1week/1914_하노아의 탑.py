#hanoi 함수의 목적은 시작점의 블록을 목표점으로 옮기는 함수로 생각한다.
def hanoi(block, start, goal, tmp):
    # 모든 동작의 재귀함수의 끝은 남은 block 이 1이고 해당 블록을 start 에서 end 로 보내면 끝이다
    # 아래가 해당 함수의 구현체이다.
    if block == 1 :
        print(start + " " + goal)
        return
    # 남은 블럭이 1개가 아닌 경우 시작점에서 남은 맨마지막 블럭을 제외한 나머지를 
    # 임시공간에 넣어야 한다. 시작점을 시작점, 목표점을 임시점, 임시점을 목표점으로 바꿔서 동작한다.
    hanoi(block-1, start, tmp, goal)
    # 위 함수가 동작되면 임시점에 남은 블록이 쌓여있는 형태이다. 따라서 다음 출력으로 이동을 표시한다. 
    print(start + " " + goal)
    # 임시점에 현재 블럭이 쌓여있는 상태로 임시점을 시작점으로 생각하고 하노아를 재귀한다.
    hanoi(block-1, tmp, goal, start)

#아래는 카운트 함수
def hanoiCnt(block, count):
    if block == 1 :
        return count + 1
    count = hanoiCnt(block-1, count)
    count += 1
    count = hanoiCnt(block-1, count)
    return count

block = int(input())
print(hanoiCnt(block, 0))
if block <= 20:
    hanoi(block, "1", "3", "2")

# 성능 최적화용
# def hanoi(n, s, g, t):
#     if n == 1 :
#         print(s + " " + g)
#         return
#     hanoi(n-1, s, t, g)
#     print(s + " " + g)
#     hanoi(n-1, t, g, s)

# n = int(input())
# 카운트 함수까지 동작시킬 수 없음... 아래 수학식으로 대체
# print(2**n-1)
# if n <= 20:
#     hanoi(n, "1", "3", "2")
# 소수 체크:
def sosu(A):
    check = True
    for i in range(2, A-1):
        if A % i == 0 :
            check = False
            break
    return check
# 중앙값 부터 골드바흐값이 소수인지 체크:
def answer(A):
    middle1 = int(A/2)
    middle2 = int(A/2)
    for i in range(1, middle1):
        if(sosu(middle1) and sosu(middle2)):
            print(middle1 , middle2)
            break
        else :
            middle1 -= 1
            middle2 += 1

for i in range(int(input())):
    A = int(input())
    answer(A)
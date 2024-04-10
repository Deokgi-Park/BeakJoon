# DP TOP-Down 방식
# 시간 초과, 메모리 초과 등등 문제 발생
# 점화식 대로 작성 : Fn = Fn-1 + Fn-2 (n ≥ 2)
# N = int(input())
# def fibo2(N):
#     if N == 0 :
#         return 0
#     if N == 1 :
#         return 1
#     return fibo2(N-2) + fibo2(N-1)
# print(fibo2(N))

# DP bottom-up 방식 
# 점화식의 동작 구상이 어려움
N = int(input())
ans = 0
before1 = 0
before2 = 1
for i in range(N):
    ans = before1+before2
    before2 = before1
    before1 = ans
print(ans)
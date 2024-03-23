# A = int(input())
B = A
for i in range(1, A):
    B *= A-i
if A==0:
    B=1 
print(B)


# 재귀함수로 동작 체크
# def factorial(n):
#     if n == 0:     
#         return 1   
#     return n * factorial(n - 1)  
# print(factorial(int(input())))
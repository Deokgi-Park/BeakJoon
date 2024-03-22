# from sys import stdin

# A = []
# B = 0
# C = 0
# for i in range(9):
#     A.append(int(stdin.readline().strip()))
    
#     if A[i] > C :
#         B = i
#         C = A[i]
    

# print(max(A))
# print(B+1)

# stdin 가 속도가 빠르다고 해서 썼으나 짧은 문인 경우 더 느린 것 같음

A = []
B = 0
C = 0
for i in range(9):
    A.append(int(input()))
    
    if A[i] > C :
        B = i
        C = A[i]
    

print(max(A))
print(B+1)

# 다음과 같이 index를 활용할 수도 있었으나, 파이선이 익숙치 않아 미사용.. print(a.index(max(a))+1)

# 유의 사항
# str 변수의 max 사용 시 앞글자 기준 사전의 순서로 가장 큰 데이터가 나온다 EX)  [가능, 가짜, 나, 가난함] => 나, [3,40,5,4000] => 5
#D = ["사", "사과", "1233", "테스트데이터"]
#print(max(D))
from collections import deque
# 파이선 자료 구조
###################################################
#3. 딕셔너리 : 중복이 제거됨
 #3-1 형태 및 선언
D = {'a':1,'b':2,'c':3,'c':3}
print(D)
 #for문으로 생성 예제
E = {x: x**2 for x in [2, 4, 6]}
print(E)

print(D['a'])
print(E[2])
print(E[4])
print(E[6])
# 키 값으로 튜플 생성 후 리스트구조로 생성 
F=E.items()
print(F)
print(F[0][0])
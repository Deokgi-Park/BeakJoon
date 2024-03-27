from collections import deque
# 파이선 자료 구조
###################################################
#3. 딕셔너리 : 중복이 제거됨
 #3-1 형태 및 선언
D = {'a':1,'b':2,'c':3,'c':3}
print(D)
 #for문으로 생성 예제
EE = [2, 4, 6]
E = {len(str(x)): x**2 for x in EE}
print(E)

print(D['a'])
print(E[1])
# 키 값으로 튜플 생성 후 리스트구조로 생성 
F=E.items()
print(F)
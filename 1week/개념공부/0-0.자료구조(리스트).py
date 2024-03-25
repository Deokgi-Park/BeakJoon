from collections import deque
# 파이선 자료 구조
###################################################
#0. 리스트
 #0-1 형태 및 선언
A = [1, 2, [3,4], 5, 5, '5']
print(A[0])
print(A[1])
print(A[2][0])
print(A[2][1])
print(A[3])
 # 문자열도 일종의 배열 취급(자바 String 같이)
X = ['123']
X[0] = X[0][1]+'2'
print('X : ', X)

 #0-2. 항목 추가
 # append : 끝에 배열 추가
print(A.append(6))
 # insert : 특정 index 뒤에 삽입
A.insert(4, 5)
print(A)
 # extend : 배열(Iterable : list, dict, set, str, bytes, tuple, range)의 각 항목[반복자](Iterator)을 모두 append 추가
A.extend('78')
A.extend([9,10])
print(A)

 #0-3. 항목 삭제
 # remove : 배열의 값을 찾아서 삭제
A.remove("7")
A.remove("8")
print(A)
 # pop : 배열의 값을 제거 후 해당 값 리턴
print(A.pop())
print(A.pop())
print(A)
 # del : 배열의 index 범위 제거
del(A[0])
del(A[0:1])
 #변수 삭제
 #del(A)
print(A)
 # clear : 배열항목 초기화
 #A.clear()
 #print(A)

 #0-4 검색 및 정렬
print(A.count(5))
 # sort : 같은형의 값을 정렬, 옵션으로 정렬방식 설정 가능
B = [1, 4, 644, 2, 1,324]
B.sort()
print(B)
C = ['나비', '가지', '다람쥐']
C.sort()
print(C)
D = ['B', 'Apple', 'ant']
D.sort()
print(D)
D.sort(reverse=True)
print(D)
 # reverse : 배열 인덱스를 역순으로 변경
B.reverse()
print(B)
 # index : 특정 값의 첫번째 index 위치 반환, 검색 index 지정가능, 해당 값이 없는 경우 에러 발생 
 # strat인 인덱스 부터, end 인덱스 전까지 검색
print(A.index(5))
print(A.index(5,1))
print(A.index(5,1,3))
 #copy : 동일 배열 복사
print(A.copy())

# *** 리스트로 큐 구현 ***
# from collections import deque
E = deque([])
E.append('A')
E.append('B')
E.append('C')
E.append('D')
print(E.popleft())
print(E.popleft())
print(E.popleft())
print(E.popleft())
print(E)

# 리스트 만드는 예제
F = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(F)
G = list(map(lambda x: x**2, range(10)))
print(G)



###################################################

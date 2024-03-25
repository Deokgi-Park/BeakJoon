#특정 횟수 반복(range 사용)
for i in range(5):
    print(i)

#특정 횟수 반복 인덱스 추가(enumerate 사용)
for i,v in enumerate(range(5)):
    print(i ,"   ", v)

# 리스트 길이만큼 반복
words=['apple','apple1','apple12','apple123']
for w in words:
    print(w, len(w))

# 딕셔너리 길이 만큼 반복 ***딕셔너리가 줄어드는 경우 .copy()를 사용한다.
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)
print(users.copy())
print(users.copy().items())

# 딕셔너리 사이즈가 for 문 중간에 변경될 경우 에러 발생
#users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#for user, status in users.items():
#    if status == 'inactive':
#        del users[user]
# >> RuntimeError: dictionary changed size during iteration

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user in users.items():
    print(user)



# 재귀 함수
def test(data, cnt) : 
    # 끝나는 조건
    if data<1 :
        print('카운트 : ' + str(cnt+1))
        return cnt+1
    #노드 분기1
    cnt = test(data-1, cnt)
    return cnt

#왼쪽에서 -1 한 경우      갯수 : 2 
#오른쪽에서 -1 한 경우    갯수 : 2
# 2 + 2 = 4
from sys import stdin
A = str(stdin.readline().strip())
B = int(A)
for i in range(9):
    up=i+1
    print(A,"*",str(up),"=",str(B*up))

# 맨처음 잘 몰랐을 때 실행, 각행마다 변수 등록를 하기 때문에 성능 나쁠것으로 보임 66ms
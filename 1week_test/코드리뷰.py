
import sys

n = int(sys.stdin.readline())
# print(n)

# 주어진 수가 1의 자리이면
if n < 10:
     n = '0'+ str(n)
     left = 0
     right = int(n)
else:
     n = str(n)
     left = int(n[0])
     right = int(n[1])

cnt =0
newNum = left + right

# 합성수가 원래 수와 같아지면 반복 종료
while True: 
     # print('사이클 진행')
     # print(newNum)

     cnt +=1
     newNum = str(newNum)

     # print('r',right, 'newR', newNum[-1])
     newNum = str(right) + newNum[-1]

     if int(n) == int(newNum):
          # print('합성수 같으면 탈출')
          break

     # 아니면 같아질때까지 반복
     right = newNum[-1] # 다음 합성수와 합칠 오른쪽 수

     # 다음 합성수 구하기
     newNum = int(newNum[0]) + int(newNum[1])
     newNum = str(newNum)
     newRight = newNum[-1]
     newNum= str(right) + str(newRight)

print(cnt)
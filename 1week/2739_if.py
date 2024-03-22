from sys import stdin
A = int(stdin.readline().strip())
for i in range(10):
    if i!=0 :
        print(A,"*",i,"=",A*i)

# 0값만 제한 40ms
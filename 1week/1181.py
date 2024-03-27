from sys import stdin

N = int(stdin.readline().strip())
A = []
for i in range(N): 
    A.append(stdin.readline().strip())
A = set(A)
A = list(A)
A.sort()
A.sort(key=len)

for i in range(len(A)): 
    print(A[i])

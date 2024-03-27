from sys import stdin

N = int(stdin.readline().strip())
A = []
for i in range(N): 
    A.append(int(stdin.readline().strip()))

A.sort()

for i in A:
    print(i)
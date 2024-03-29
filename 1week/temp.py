import sys
M,N,L = map(int, sys.stdin.readline().split())
pos = list(map(int, sys.stdin.readline().split()))
pos.sort()
animals = [list(map(int, sys.stdin.readline().split())) for x in range(N)]
print(M,N,L)
print(pos)
print(animals)
from sys import stdin

def solve(a, b):
    anw = ""
    for c in b :
        anw += c*a
    print(anw)

i = int(input())
for x in range(0,i):
    A,B = input().split()
    solve(int(A),B)
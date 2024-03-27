from sys import stdin
from typing import MutableSequence
def qsort(a :MutableSequence, l:int, r:int):
    pl = l
    pr = r
    mid = a[(l+r)//2]

    while pl <= pr:
        while a[pl] < mid : pl +=1
        while a[pr] > mid : pr -=1
        if pl <= pr:
            a[pl],a[pr] = a[pr],a[pl]
            pl += 1
            pr -= 1
    if l < pr: qsort(a, l , pr)
    if pl < r : qsort(a, pl, r)

N = int(stdin.readline().strip())
A = []
for i in range(N): 
    A.append(int(stdin.readline().strip()))

qsort(A,0,len(A)-1)
for i in range(N): 
    print(A[i])
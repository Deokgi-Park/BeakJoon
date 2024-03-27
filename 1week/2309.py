def loo(A:list):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            B = A.copy()
            rm1 = B[i]
            rm2 = B[j]
            B.remove(rm1)
            B.remove(rm2)
            if sum(B) == 100 :
                return B

A = []
for i in range(9):
    A.append(int(input()))
C = loo(A)
C.sort()

for x in C:
    print(x)
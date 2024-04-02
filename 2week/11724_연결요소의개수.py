import heapq
V, E = map(int,input().split())


status = [0]
data = []
for i in range(E):
    data.append(list(map(int, input().split())))
for i in range(1, V+1):
    status.append(i)


heapq.heapify(data)

result = 0
def cul():
    for i in range(E):
        v = heapq.heappop(data)
        a = parent_checker(v[0])
        b = parent_checker(v[1])
        if a != b:
            status[max(a,b)] = min(a,b)


def parent_checker(i):
    if status[i] != i:
        return parent_checker(status[i])
    else:
        return status[i]

cul()

for i in range(1,len(status)) :
    if status.count(i) > 1:
        result += 1 

print(result)

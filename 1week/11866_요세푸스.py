from collections import deque
data = input().split(' ')
q = deque([])
for x in range(1, int(data[0])+1):
    q.append(str(x))
x = 1
remake = []
prefix = "<"
endfix = ">"
while len(q) != 0 :
    if x%int(data[1]) == 0:
        remake.append(q.popleft())
    else:    
        q.append(q.popleft())
    x += 1


print(prefix+', '.join(x for x in remake)+endfix)
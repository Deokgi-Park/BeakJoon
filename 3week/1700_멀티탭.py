import sys
n , k = map(int,sys.stdin.readline().split())
graph = list(map(int,sys.stdin.readline().split()))

hole = []
old = 0
cnt = 0
for i in range(k):
    if len(hole) < n :
        if graph[i] not in hole:
            hole.append(graph[i])
    elif graph[i] in hole:
        continue
    else :
        differ = graph[i+1:]
        changeVal = 0
        for data in hole:
            try:
                before = differ.index(changeVal)
            except:
                before = -1
            try:    
                after = differ.index(data)
            except:
                after = -1
            if after == -1 : 
                changeVal = data
                break
            if before < after :
                changeVal = data
        if graph[i] not in hole:
            hole.remove(changeVal)
            hole.append(graph[i])
            cnt +=1
print(cnt)
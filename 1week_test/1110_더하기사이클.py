i = input()

def mergedata(n):
    global i
    cnt = 1
    if len(n) == 1:
        n = "0"+n
    sumdata = str(int(n[0])+int(n[1]))
    n = n[1]+sumdata[-1]
    if n[0] == "0" :
        n = n[1]
    while i != n:
        cnt +=1
        if len(n) == 1:
            n = "0"+n
        sumdata = str(int(n[0])+int(n[1]))
        n = n[1]+sumdata[-1]
        if n[0] == "0" :
            n = n[1]
    return cnt

print(mergedata(i))

def allset(n, x, data):
    if x >= n :
        print(data)
    else:
        for i in range(n):    
            data[x] = i
            allset(n, x+1, data)
            
data = [0] * 4
allset(4, 0, data)
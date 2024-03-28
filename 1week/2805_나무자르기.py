info = list(map(int, input().split(' ')))
tree = list(map(int, input().split(' '))) 
start = 1
end = max(tree)

def cut(start, end, info, tree):
    sum = 0
    mid = (start+end) // 2
    for i in tree:
        if i > mid:
            sum += i - mid
    if start > end:
        print(end)
        return
    elif sum < info[1] :
        cut(start, mid-1, info, tree)
    else :
        cut(mid+1, end, info, tree)

cut(start, end, info, tree)
import sys
prenode = []
tree = {}
i = 0
while True:
    try:
        prenode.append(int(input()))
        tree[prenode[i]] = [0, 0]
        i+=1
    except:
        break


rootnode = prenode[0]
prevalue = 0

print(tree)
def preTolast(nownode, prevalue):
    global rootnode
    if prenode :
        if rootnode >= prenode[0] :    
            if nownode >= prenode[0] :
                prevalue = nownode
                tree[nownode][0] = prenode[0]
                prenode.remove(prenode[0])
                preTolast(tree[nownode][0], prevalue)
            else :
                tree[prevalue][1] = prenode[0]
                prenode.remove(prenode[0])
                preTolast(tree[prevalue][1], prevalue)
        else :
            if rootnode < prenode[0] :
                tree[rootnode][1] = prenode[0]
                rootnode = prenode[0]
                preTolast(tree[nownode][0] ,prevalue)
            if nownode >= prenode[0] :
                prevalue = nownode
                tree[nownode][0] = prenode[0]
                prenode.remove(prenode[0])
                preTolast(tree[nownode][0] ,prevalue)
            else :
                tree[prevalue][1] = prenode[0]
                prenode.remove(prenode[0])
                preTolast(tree[prevalue][1], prevalue)


preTolast(rootnode, prevalue)
print(tree)
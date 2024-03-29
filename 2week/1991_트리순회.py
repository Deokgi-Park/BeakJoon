N = int(input())

tree = {}
for i in range(N):
    root, left, right = input().split(' ')
    tree[root] = [left, right]
# tree = {
#     "A":["B","C"],
#     "B":["D","."],
#     "C":["E","F"],
#     "E":[".","."],
#     "F":[".","G"],
#     "D":[".","."],
#     "G":[".","."]
#     }

print(tree["A"])

def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])
def middle(root):
    if root != '.':
        middle(tree[root][0])
        print(root, end='')
        middle(tree[root][1])
def lastnode(root):
    if root != '.':
        lastnode(tree[root][0])
        lastnode(tree[root][1])
        print(root, end='')
pre("A")
print()
middle("A")
print()
lastnode("A")
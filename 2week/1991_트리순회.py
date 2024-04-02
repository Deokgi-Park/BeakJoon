N = int(input())
node = {}
for _ in range(N):
    data = input().split()
    node[data[0]] = [data[1],data[2]]

def run(start):
        if start != '.':
            print(start,end='')
            run(node[start][0])
            run(node[start][1])
def run1(start):
        if start != '.':
            run1(node[start][0])
            print(start,end='')
            run1(node[start][1])
def run2(start):
        if start != '.':
            run2(node[start][0])
            run2(node[start][1])
            print(start,end='')
run('A')
print()
run1('A')
print()
run2('A')


































# N = int(input())

# tree = {}
# for i in range(N):
#     root, left, right = input().split(' ')
#     tree[root] = [left, right]
# # tree = {
# #     "A":["B","C"],
# #     "B":["D","."],
# #     "C":["E","F"],
# #     "E":[".","."],
# #     "F":[".","G"],
# #     "D":[".","."],
# #     "G":[".","."]
# #     }

# print(tree["A"])

# def pre(root):
#     if root != '.':
#         print(root, end='')
#         pre(tree[root][0])
#         pre(tree[root][1])
# def middle(root):
#     if root != '.':
#         middle(tree[root][0])
#         print(root, end='')
#         middle(tree[root][1])
# def lastnode(root):
#     if root != '.':
#         lastnode(tree[root][0])
#         lastnode(tree[root][1])
#         print(root, end='')
# pre("A")
# print()
# middle("A")
# print()
# lastnode("A")
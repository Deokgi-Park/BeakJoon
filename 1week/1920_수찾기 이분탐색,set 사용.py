# 이분 탐색 수행

# N = int(input())
# data = list(map(int, input().split()))
# M = int(input())
# find = list(map(int, input().split()))
# data.sort()

    
# def binary_search(array, target, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return 1
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
# for one in find :
#     print(binary_search(data, one, 0, len(data)-1))



# set 사용
input()
N = set(input().strip().split(' '))
input()

for M in input().strip().split(' '):
    if M in N:
        print('1')
    else:
        print('0')
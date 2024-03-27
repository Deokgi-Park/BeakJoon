import heapq
import sys

arr = []

for N in range(int(sys.stdin.readline())):
  x = int(sys.stdin.readline())
  if x != 0:
    heapq.heappush(arr, (-x, x))
  else:
    try:
      print(heapq.heappop(arr)[1])
    except:
      print(0)


# import sys

# N = int(sys.stdin.readline().strip())
# arr = []
# setdata = {0}

# for N in range(int(sys.stdin.readline())):
#     i = int(sys.stdin.readline())
#     if i == 0:
#         print(max(setdata))
#         if max(setdata) != 0 :
#             setdata.remove(max(setdata))
#     else:
#         setdata.add(i)

# print(max(setdata))

# import sys

# N = int(sys.stdin.readline().strip())
# def heap_sort(a):
#     def down_heap(a, left, right):
#         temp = a[left]

#         parent = left
#         while parent < (right +1) // 2:
#             cl = parent * 2 + 1
#             cr = cl + 1
#             child = cr if cr <= right and a[cr]>a[cl] else cl
#             if temp >= a[child]:
#                 break
#             a[parent] = a[child]
#             parent = child
#         a[parent] = temp

#     n = len(a)

#     for i in range((n-1)//2, -1,-1):
#         down_heap(a, i, n-1)
#     for i in range(n-1, 0, -1):
#         a[0],a[i] = a[i], a[0]
#         down_heap(a, 0, i-1)

# x = [9, 7, 8, 12, 64, 1, 0]
# print(x)

# 힙공부
#  import sys
# def down_heap(a, left, right):
#     temp = a[left]
#     parent = left
#     while parent < (right +1) // 2:
#         cl = parent * 2 + 1
#         cr = cl + 1
#         child = cr if cr <= right and a[cr]>a[cl] else cl
#         if temp >= a[child]:
#             break
#         a[parent] = a[child]
#         parent = child
#     a[parent] = temp

# N = int(sys.stdin.readline().strip())
# d = [sys.stdin.readline().strip() for _ in range(N)]
# for i in range((N-1)//2, -1,-1):
#     down_heap(d, i, N-1)
# for i in range(N-1, 0, -1):
#     d[0],d[i] = d[i], d[0]
#     down_heap(d, 0, i-1) 

# print(d)
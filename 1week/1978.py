q = int(input())
num = input().split()

cnt = 0
for one in num:
    check = True
    for i in range(2, int(one)-1):
        if int(one) % i == 0 :
            check = False
            break
    if int(one) == 1:
       check = False 
    if check :
        cnt = cnt+1

print(cnt)



# q = int(input())
# num = list(map(int, input().split()))

# cnt = 0
# for one in num:
#     check = True
#     for i in range(2, int(one)):
#         if one % i == 0 :
#             check = False
#             break
#     if one == 1:
#        check = False 
#     if check :
#         cnt = cnt+1

# print(cnt)
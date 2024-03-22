from sys import stdin

A = int(stdin.readline())
if A >= 90 :
    print('A')
elif 89 >= A >= 80 :
    print('B')
elif 79 >= A >= 70 :
    print('C')
elif 69 >= A >= 60 :
    print('D')
else :
    print('F')
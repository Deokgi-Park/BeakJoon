def hanoi(n, s, g, t):
    if n == 1 :
        print(s + " " + g)
        return
    hanoi(n-1, s, t, g)
    print(s + " " + g)
    hanoi(n-1, t, g, s)

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, "1", "3", "2")
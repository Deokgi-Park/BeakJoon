def test(n):
    if n <= 1: 
        return 1
    return test(n-1) + test(n-2)
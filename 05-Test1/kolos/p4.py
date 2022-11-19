def f(n):
    a = 0
    b = 1
    c = 0
    for i in range(0,n):
        c+=a
        a=b
        b=c
    return c
def f(p1,p2):
    p1 = list(p1)
    p2 = list(p2)

    sum1 = 0
    sum2 = 0

    for i in p1:
        if i in ["T", "J", "Q", "K", "A"]:
            sum1+=10
        else: 
            sum1 += int(i)
    
    for j in p2:
        if j in ["T", "J", "Q", "K", "A"]:
            sum2+=10
        else: 
            sum2 += int(j)

    return sum1 > sum2
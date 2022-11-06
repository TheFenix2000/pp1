def f(number, even):
    sumOfNumbers = 0
    if even == True:
        num = str(number)
        for i in num:
            if int(i) % 2 == 0:
                sumOfNumbers += int(i)
        return sumOfNumbers
    else:
        num = str(number)
        for i in num:
            if int(i) % 2 != 0:
                sumOfNumbers += int(i)
        return sumOfNumbers

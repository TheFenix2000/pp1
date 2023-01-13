def f(dictionary, x, y):
    suma = 0
    for key in dictionary:
        for num in dictionary[key]:
            if x<= num <=y:
                suma+=num
    return suma


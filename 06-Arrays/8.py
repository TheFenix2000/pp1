arr = [-15, 8, -31, 47, -2, 19]
def minMax(arr):
    min = 0
    max = 0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    print(min, max)
minMax(arr)
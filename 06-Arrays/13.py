arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
def sumEven(arr):
    sumOfE = 0
    for i in arr:
        for j in i:
            if j%2==0:
                sumOfE+=j
    print(sumOfE)
sumEven(arr)
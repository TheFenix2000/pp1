# def f(array2D):
#     suma1 = 0
#     suma2 = 0
#     suma3 = 0
#     suma4 = 0
#     for i in array2D:
#         suma1+=i[0]
#         suma2+=i[1]
#         suma3+=i[2]
#         suma4+=i[3]
#     return [suma1, suma2, suma3, suma4]

def f(array2D):
    suma=[]

    for i in range(len(array2D[0])):
        sum_col = 0
        for j in range(len(array2D)):
            sum_col += array2D[j][i]
        suma.append(sum_col)
    return suma

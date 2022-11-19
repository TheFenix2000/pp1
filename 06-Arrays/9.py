arr = ["Genowefa", "Alojzy", "Marek", "Maksymilian"]
def longest(arr):
    long = ""
    leng = 0
    for i in arr:
        if len(i) > leng:
            leng = len(i)
            long = i
    print(long)
longest(arr)

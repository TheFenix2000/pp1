def isDivisable(rangeMy = 30 ):
    result = ""
    for num in range(1,rangeMy+1):
        if num % 3 == 0 and num % 5 != 0:
            result += "THREE "
        elif num % 5 == 0 and num % 3 != 0:
            result += "FIVE "
        elif num % 5 == 0 and num % 3 == 0:
            result += "BINGO "
        else: result += str(num) + " "
    print(result)

isDivisable(70)

def f(amount_to_pay):
    numberOfFives = 0
    numberOfTwos = 0
    numberOfOnes = 0

    while amount_to_pay >= 5:
        numberOfFives+=1
        amount_to_pay -=5

    while amount_to_pay >= 2:
        numberOfTwos+=1
        amount_to_pay -=2

    while amount_to_pay >= 1:
        numberOfOnes+=1
        amount_to_pay -=1
    sumOfCoins = numberOfOnes + numberOfTwos + numberOfFives
    
    return sumOfCoins

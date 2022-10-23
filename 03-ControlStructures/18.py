price = int(input("Enter a price: "))
print(f"Given price: {price}")
numberOfFives = 0
numberOfTwos = 0
numberOfOnes = 0

while price >= 5:
    print(price)
    numberOfFives+=1
    price -=5
    print(price)

while price >= 2:
    print(price)
    numberOfTwos+=1
    price -=2
    print(price)

while price >= 1:
    print(price)
    numberOfOnes+=1
    price -=1
    print(price)

print(f"Number of 5's: {numberOfFives}")
print(f"Number of 2's: {numberOfTwos}")
print(f"Number of 1's: {numberOfOnes}")

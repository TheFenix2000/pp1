humanYears = int(input("Enter dog age in human years: "))

dogYears = ((humanYears - 2) * 4) + 21 if humanYears > 2 else humanYears * 10.5

print(f"The dog's age in dog's years is {dogYears} years.")
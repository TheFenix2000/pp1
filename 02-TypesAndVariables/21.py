import random

rand = random.randrange(1, 7)
answer = int(input("Try to guess what number I rolled: "))

if answer != rand:
    print(False,f"It was {rand}")
else: print(True)
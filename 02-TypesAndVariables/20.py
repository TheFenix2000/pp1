import random


suma = 0
for i in range(1,4):
    rand = random.randrange(1,7)
    print(f"{i}. Roll: {rand}")
    suma += rand
print(f"Sum of 3 rolls: {suma}")
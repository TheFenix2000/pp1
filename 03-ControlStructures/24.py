import math
length = 9
line = "* "
middle = math.ceil(length / 2)
for i in range(1, length+1):
    if i <= middle:
        print(line*i)
    else: 
        middle -= 1
        print(line*middle)

import math
cm = int(input("Enter height: "))

ft = cm / 30.48

inch = 12*(ft%math.floor(ft))

print(f"I am {cm}cm tall, i.e. {math.floor(ft)} ft and {round(inch)} inches")

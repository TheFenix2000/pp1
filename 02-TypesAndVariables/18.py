a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

p = (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**.5
print(f"Area: {area:.2f}")
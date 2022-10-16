import math
#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
radius = 5
pi = math.pi

# calculate area
area = pi * pow(radius, 2)

# calculate circumference
cir = 2 * pi * radius

# display results
print(f"Area: {area:.3f}\nCircumference: {cir:.3f}")

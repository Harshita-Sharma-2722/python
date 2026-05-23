import math
def circle(radius):
    diameter=2*radius
    area=3.14*radius*radius
    return diameter,area
r = float(input("Enter radius = "))
d, a = circle(r)
print("Diameter =", d)
print("Area =", a)
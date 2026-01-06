# Area and perimeter of a triangle
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

p = a + b + c
s = p / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Perimeter =", p)
print("Area =", area)

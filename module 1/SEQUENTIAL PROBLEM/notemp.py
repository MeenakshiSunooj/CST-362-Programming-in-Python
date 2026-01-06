#Swap 2 numbers without using a temporary variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)

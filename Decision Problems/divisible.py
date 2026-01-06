# Check whether a number is completely divisible by another number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a % b == 0:
    print("Completely divisible")
else:
    print("Not divisible")
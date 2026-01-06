# Find the large digit in a two-digit number
n = int(input("Enter two digit number: "))

a = n // 10
b = n % 10

if a > b:
    print("Largest digit =", a)
else:
    print("Largest digit =", b)
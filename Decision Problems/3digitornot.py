#Check whether a number is 3-digit or not
n = int(input("Enter number: "))

if n >= 100 and n <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")
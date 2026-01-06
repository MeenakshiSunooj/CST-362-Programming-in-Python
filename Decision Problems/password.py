#Check password strength
pwd = input("Enter password: ")

l = len(pwd)

if l < 6:
    print("Weak")
elif l <= 10:
    print("Medium")
else:
    print("Strong")

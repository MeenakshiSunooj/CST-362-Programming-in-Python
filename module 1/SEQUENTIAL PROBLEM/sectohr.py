# Convert seconds to hours : minutes : seconds
sec = int(input("Enter seconds: "))

h = sec // 3600
m = (sec % 3600) // 60
s = sec % 60

print(h, ":", m, ":", s)


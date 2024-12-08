
num = int(input("Enter any number : "))
multi = int(input("Enter number of multiple : "))
s = 0

for e in range(1, multi+1):
    s = s+num*e

print("Sum is : ", s)

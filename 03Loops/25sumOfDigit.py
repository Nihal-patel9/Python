
num = int(input("Enter a Number : "))
s = 0

while num:
    s = s+num % 10
    num = num//10

print(s)


a, b = -1, 1
l2 = []

n = int(input("Enter a number : "))
while n:
    c = a+b
    l2.append(c)
    a = b
    b = c
    n -= 1

print(l2)

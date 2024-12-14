
# create a list of first N prime number

n = int(input("Enter a number : "))
l2 = []
x = 2
while n:
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        l2.append(x)
        n -= 1
    x += 1

print(l2)

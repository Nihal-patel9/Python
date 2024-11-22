

# print natural number reverse using range

number = int(input("Enter a number = "))
r = range(number*2, 1, -2)


for e in r:
    print(e, end=' ')

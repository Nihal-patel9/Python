
# print natural number square using range

number = int(input("Enter a number = "))
r = range(1, number+1)


for e in r:
    print(e**2, end=' ')

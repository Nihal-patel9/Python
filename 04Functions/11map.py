
def square(a):
    return a*a


x = map(square, [1, 2, 3, 4])
print(x)

for e in x:
    print(e, end=" ")

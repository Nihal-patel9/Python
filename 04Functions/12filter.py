
def f(x):
    if x % 2 == 0:
        return x


t = (10, 2, 0, -4, 5, 8, 19, 9)
y = filter(f, t)
print(y)

for e in y:
    print(e, ' ')

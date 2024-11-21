n = int(input("Enter your number to find factorial = "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(n)
print(result)

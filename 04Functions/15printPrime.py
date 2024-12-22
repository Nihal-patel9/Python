
# print range in prime number

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def printPrimeRange(a, b):
    x = a+1
    while x < b:
        if isPrime(x):
            print(x, end=' ')
        x += 1


printPrimeRange(10, 20)

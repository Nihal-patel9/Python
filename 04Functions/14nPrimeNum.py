
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def nextPrime(num):
    num += 1
    while (not isPrime(num)):
        num += 1
    return num


def printPrime(n):
    x = 2
    for i in range(1, n+1):
        print(x, end=' ')
        x = nextPrime(x)


printPrime(10)

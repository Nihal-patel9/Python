# Compute the factorial of a number using a while loop.


number = int(input("Enter any Number = "))
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)

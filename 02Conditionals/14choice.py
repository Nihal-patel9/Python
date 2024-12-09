
print(" 1. Even Odd")
print(" 2. Positive and non-positive")
print(" 3. Leep Year")


num = int(input("Enter your choice : "))

match num:
    case 1:
        print("Enter a number : ")
        n = int(input())
        print("Even" if n % 2 == 0 else "Odd")

    case 2:
        print("Enter a number")
        n = int(input())
        print("Positive" if n > 0 else "non - positive ")

    case 3:
        print("Enter any year")
        n = int(input())
        print("Leep year" if n % 4 == 0 else "not leep year ")

    case _:
        print("Invalid choice")

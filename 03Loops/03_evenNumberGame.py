# find even number game

i = 1
while i <= 3:
    num = int(input("Enter an even Number (you have only 3 chance) = "))
    if num % 2 == 0:
        break
    i += 1

if i == 4:
    print("You lost the game")
else:
    print("You won the game")

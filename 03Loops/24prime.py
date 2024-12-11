
# check prime number in given start and end number

start = int(input("Enter start value : "))
end = int(input("Enter start value : "))

for x in range(start, end):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        print(x, end=" ")

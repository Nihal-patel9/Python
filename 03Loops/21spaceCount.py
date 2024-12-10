# spece count in given string

s = input("Enter a string : ")

count = 0

for e in s:
    if e == ' ':
        count += 1

print("Count : ", count)

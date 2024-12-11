# remove repeted Number

s = input("Enter any number : ")

i = 0

for e in s:
    if s.index(e) == i:
        print(e, end=" ")
    i += 1

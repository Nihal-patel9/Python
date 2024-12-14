
# check given string has only alphabets

s1 = input("Enter a string : ")
for e in s1:
    if e >= 'a' and e <= 'z' or e >= 'A' and e <= 'Z':
        pass
    else:
        print("String has at least one character which is not an alphabets")
        break
else:
    print("String contains only alphabets")

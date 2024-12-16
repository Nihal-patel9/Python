
# vowel count in given string

count = 0
s1 = input("enter a string : ")
for e in s1:
    if e in "aeiouAEIOU":
        count += 1

print("Vowel Count  = ", count)

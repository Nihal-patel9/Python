
# count word in string

s1 = input("Enter a string : ")
s1.strip()
l1 = s1.split(' ')
print(l1)
i = 0
wordCount = 0
while i < len(l1):
    if l1[i] != '':
        wordCount += 1
    i += 1

print("Total Words : ", wordCount)

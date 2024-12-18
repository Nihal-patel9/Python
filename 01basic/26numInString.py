
# extract num in given string

s1 = input("Enter a string include number : ")
l1 = []
for word in s1.split(' '):
    try:
        l1.append(float(word))
    except:
        pass

print(l1)

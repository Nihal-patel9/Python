
# check character is present in a given string or not

s1 = input("Enter a String : ")
ch = input("Enter a character : ")

if ch in s1:
    print("%s is in %s" % (ch, s1))
else:
    print("%s is not in %s" % (ch, s1))

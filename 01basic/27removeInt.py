
# remove all int value in list

l1 = [20, 10, 30.00, 3+4j, 'abc', True, 60]
i = 0
l2 = []
while (i < len(l1)):
    if type(l1[i]) == int:
        l2.append(l1[i])
    i += 1

print(l2)

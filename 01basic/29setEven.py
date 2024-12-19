
s1 = {10, 12, 49, 70, 40, 21, 16}
odd = set()
even = set()
for e in s1:
    if e % 2 == 0:
        even.add(e)
    else:
        odd.add(e)

print(even, odd)

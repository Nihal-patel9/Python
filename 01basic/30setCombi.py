
s1 = {'Virat', 'Rahul', 'Sachin', 'Dhoni', 'Kapil'}
i = 0
for p1 in s1:
    i += 1
    for p2 in list(s1)[i::]:
        print(p1, p2)

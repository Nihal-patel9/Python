
def lcm(a, b):
    L = a if a > b else b
    while L <= a*b:
        if L % a == 0 and L % b == 0:
            break
        L += 1
    print("LCM is : ", L)


lcm(4, 6)

def gcd(a,b):
    if a<b:
        return gcd(a,b-a)
    elif b<a:
        return gcd(a-b,b)
    else:
        return a
print(gcd(68,119))

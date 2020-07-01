def gcd(a,b):
    if a == 0 :
        return b
    if b == 0:
        return a
    if a>=b:
        r = a%b
        a=r
    else:
        r= b%a
        b=r
    return gcd(a, b)

print(gcd(1000,1000))
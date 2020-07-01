def prime_num(x):
    y = int(x**0.5)+1
    for i in range (2, y):
        z=x%i
        if z==0:
            return False
    
    return True

print(prime_num(101))

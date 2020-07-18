def power(x,n):
    if n ==0:
        return 1
    # if n ==1:
    #     return x
    if n>=0:
        return x*power(x,n-1)
    if n<0:
        return 1/(x*power(x,-n-1))


print(power(2,4))

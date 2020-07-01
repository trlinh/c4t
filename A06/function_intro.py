def calc_delta(a,b,c):
    return b*b - 4*a*c
def quadratic(a,b,c):
    delta= calc_delta(a,b,c)
    if delta<0:
        return None
    if delta == 0:
        x = -b/2/a
        return  x
    if delta > 0:
        x1 = (-b+delta**0.5)/(2*a)
        x2 = (-b-delta**0.5)/(2*a)
        return x1, x2

# print("nghiem phuong trinh", quadratic(1,-3,2))

def arr_sum(arr):
    sum = 0
    for i in range(len(arr)): 
        sum = sum + arr[i]
        
    return sum
# for i in arr:
#     sum +=i
arr=[1,2,3,4,5,6,7]
print(arr_sum(arr))


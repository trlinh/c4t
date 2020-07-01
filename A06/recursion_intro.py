arr = [2,1,5,9,8,7,0,6,4,3]
def sum(arr):
   
    if len(arr)==1:  # anchor
        return arr[0]
    mid = len(arr)//2
    left = sum(arr[0:mid])
    right = sum(arr[mid:])
    return left + right
# print(sum(arr))


def reverse(string):
    if len(string) ==1:
        return string[0]
    if len(string) ==2:
        return string[1]+string[0]
    mid = len(string)//2
    return  reverse(string[mid:]) + reverse(string[0:mid])
# if len(string)==1:
#     return string
# return reverse(string[1:])+string[0]

# print(reverse(string="1234567890"))

# n!=n(n-1)!=n(n-1)(n-2)!

def factorial(n):
    if n==1: 
        return 1
    return n*factorial(n-1)

# print(factorial(4))

arr = [2,1,5,9,8,7,0,6,4,3]

# def sum(arr):
#     if len(arr)==1:
#         return arr[0]
#     mid=len(arr)//2
#     left=arr[0:mid]
#     right=arr[mid:]
#     return sum(left)+sum(right)

# print(sum(arr))

def min(arr):
    if len(arr)==1:
        return arr[0]
    mid=len(arr)//2
    left=arr[0:mid]
    right=arr[mid:]
    if min(left)>min(right):
        return min(right)
    return min(left)

def reverse(string):
    if len(string)==1:
        return string[0]
    return reverse(string[1:])+string[0]

print(reverse(string="1234567890-"))

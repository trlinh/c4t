def repeat(arr, x):
    if len(arr)==1:
        if arr[0]!=x:
            return 0
        return 1
    mid = len(arr)//2
    left = repeat(arr[0:mid],x)
    right = repeat(arr[mid:],x)
    return left  + right

arr=[1,2,3,4,5,6,7,8,9,0,1,1,1,1]
x=2
print(repeat(arr, x))
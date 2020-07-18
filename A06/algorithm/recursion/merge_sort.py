def merge(left,right):
    arr=[]
    while(len(left)*len(right)>0):
        if left[0]>right[0]:
            arr.append(right[0])
            right.pop(0)
            
        else:      
        
            arr.append(left[0])
            left.pop(0)
    arr +=(left+right)
    return arr


def sort(arr):
    
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    left = sort(arr[0:mid])
    right = sort(arr[mid:])
    return merge(left,right)
    
a=[1,4,3,5,6,0,90,-1,-100,90.5]
print(sort(a))
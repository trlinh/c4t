def binary_search(arr, x, high, low):
    
    
    if low <=high:
        
        mid = (high+low)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            return binary_search(arr,x,mid-1,low)
        else:
            return binary_search(arr,x,high,mid+1)
    return -1


a=[1,2,3,4,5,6,7,8,9]

print(binary_search(a,0,len(a)-1,0))



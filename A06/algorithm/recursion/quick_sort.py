def partition(arr):
    pivot=arr[-1]
    start = 0
    for i in  range(len(arr)):
        if arr[i] <= pivot:
            temp = arr[start]
            arr[start]=a[i]
            a[i] = temp
            start+=1
    return start, arr

def quick_sort(arr):
    print(arr)
    if len(arr)==0:
        return arr
    # if len(arr)==1:
    #     return arr
    mid, arr = partition(arr)
    left = quick_sort(arr[0:mid-1])
    right = quick_sort(arr[mid:])   

    arr = left + [arr[mid-1]] + right
    return arr
    
a=[8,4,3,7,1,2,6,5]
print(quick_sort(a))




partition(a)
# print(a)

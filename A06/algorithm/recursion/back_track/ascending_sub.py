
def ascending_sub(arr, sub_set=[], i=0):
    
    if i == len(arr):
        # x = len(sub_set)
        # print(x,sub_set)
        return sub_set
        
        
    if i <len(arr):
        if len(sub_set)==0:
            left=ascending_sub(arr, sub_set+[arr[i]], i+1)
            right=ascending_sub(arr, sub_set, i+1)
            if len(left)>len(right):
                return left
            return right
        if len(sub_set)>=1:
            if sub_set[-1]<arr[i]:
                left=ascending_sub(arr, sub_set+[arr[i]], i+1)
                right=ascending_sub(arr, sub_set, i+1)
                if len(left)>len(right):
                    return left
                return right
            if sub_set[-1]>arr[i]:
                return ascending_sub(arr, sub_set, i+1)



a=[1,3,2,4,6,8,10]
print(ascending_sub(a))

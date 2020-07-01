arr = [7, 4, 3, 1, 5, 2, 6]

for i in range(len(arr)-1):

    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
           
            temp=arr[j+1]
            arr[j+1]=arr[j]
            arr[j]=temp
            j = j+1
print(arr)
arr = [7, 4, 3, 1, 5, 2, 6]
for i in range(1, len(arr)): 
  
    key = arr[i] 

    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            # arr[j] = key 

            j -= 1
    arr[j+1] = key 
    
print(arr)

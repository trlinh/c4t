arr = [7, 4, 3, 1, 5, 2, 6]

n = len(arr)

# for i in range(n):
#     min = arr[i]
#     print(min)
#     for j in  range(i, n-i):
#         # print(arr)
#         arr.remove(min)
#         arr.insert(i, min)
#         for j in  range(i, n-i):
#             if min > arr[j]:
#                 min = arr[j]
#             # arr.remove(min)
#             # arr.insert(i, min)

# print(arr)


min = arr[0]
for i in range(n-1):
    min_index=i
    for j in range(i, n):
        if arr[min_index] > arr[j]:    
            min_index = j
       
    temp = arr[min_index]
    arr[min_index] = arr[i]
    arr[i] = temp
    
print(arr)
    
    


    
    
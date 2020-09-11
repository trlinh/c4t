def sub_set(arr,i=0, sub_arr=[]):
    
    if i==len(arr):
       
        print(sub_arr)
    if i<len(arr):
        sub_set(arr,i+1,sub_arr+[arr[i]])
        sub_set(arr,i+1,sub_arr)
                
   

arr=[1,2,3,5,8]
sub_set(arr)



#bẻ mảng thành 2 mảng con có tổng giá trị các phần tử bằng nhau, mảng bất kì nếu có thì in nếu không có thì thôi
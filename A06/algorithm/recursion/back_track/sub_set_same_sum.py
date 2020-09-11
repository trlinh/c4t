def same_sum(arr,i=1,sub_set1=[],sub_set2=[]):
    if i==len(arr):
        sum1=0
        sum2=0
        for j1 in sub_set1:
            sum1+=j1
        for j2 in sub_set2:
            sum2+=j2
        if sum1==sum2:
                
            print(sub_set1,sub_set2)
            print(sum1,sum2)
        
    sub_set1=[arr[0]]    
    if i<len(arr):
        
        same_sum(arr,i+1,sub_set1+[arr[i]],sub_set2)
        same_sum(arr,i+1,sub_set1,sub_set2+[arr[i]])
        # same_sum(arr,i+1,sub_set1,sub_set2)


a=[5,7,2]
same_sum(a)
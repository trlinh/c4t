def coin_choose(n,arr,choose=[],i=0):
    if n ==0:
        
        print(choose) 
    if n>0:
        # for i in range(len(arr)):
        for j in range(i,len(arr)):
            coin_choose(n-arr[j],arr,choose+[arr[j]],j)


a=[1,2,5,10,20,50,100]

coin_choose(100,a)

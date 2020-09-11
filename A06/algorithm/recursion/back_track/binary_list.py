def binary_list(n,list=[]):
    if n==0:
        print(list) 
    if n>0:
        for i in [0,1]:
            binary_list(n-1,list+[i])
    
# binary_list(3)


def bit_string(n,bit=""):
    if n==0:
        print(bit)
    if n>0:
        bit_string(n-1,bit+"0")
        bit_string(n-1,bit+"1")

bit_string(3)
cot_a=[1,2,3,4,5]
cot_b=[]
cot_c=[]

def move(n,cot_1,cot_2,cot_3):
    # anchor
    if n == 1:
        cot_2.insert(0,cot_1.pop(0))
        
    else:
        # chuyen n-1 vong tu xp-> tg
        move(n-1,cot_1,cot_3,cot_2)
        # chuyen vong n tu n tu xp -> dich
        cot_2.insert(0,cot_1.pop(0))
        # chuyen n-1 vong tu tg -> dich
        move(n-1,cot_3,cot_2,cot_1)
        
        
    # cot_dich.insert(0,cot_tg.pop(n-1))

move(5,cot_a,cot_b,cot_c)
print(cot_b)
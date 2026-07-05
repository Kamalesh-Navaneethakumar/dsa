#largedih

def largedih(n):
    large=n%10
    n//=10
    while n>0:
        digi=n%10
        large =max(large,digi)
        #if digi<large:
            #large=digi
        n//=10
    return large 
print(largedih(54962))




 
        


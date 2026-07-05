#secondlargestdih
def secondlargedih(n):
    large=0
    second =0
    while n>0:
        digi=n%10
        if digi>large :
            second = large 
            large= digi
        if digi<large and digi >second:
            second = digi
        n//=10 
    return second




print(secondlargedih(6783))   
print(secondlargedih(99931))  
print(secondlargedih(1111))   



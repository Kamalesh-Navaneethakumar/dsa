def pali(n):
    rev =0
    x=abs(n)
    while x>0:
        digi=x%10
        rev=rev*10+digi
        x//=10
    if rev==n:
        return True
    else:
        return False 


print(pali(123))
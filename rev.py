#reverse

def rev(n):
    rev=0
    if n>0:
        while n>0:
            digi= n%10
            rev = rev*10+digi
            n//=10
        return rev
    else:
        while n<0:
            digi=n%-10
            rev= rev*10+digi
            n= int(n/10)
        return rev





print(rev(654))
print(rev(-654))
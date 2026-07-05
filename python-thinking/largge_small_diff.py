def diff(n):
    large=n%10
    small=n%10
    n//=10
    while n>0:
        digi = n%10
        if digi >large:
            large =digi
        if digi < small:
            small= digi
        n//=10
    return large-small

print(diff(7678))
        


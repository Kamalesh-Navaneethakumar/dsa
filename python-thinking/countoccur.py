def countocu(n,digi):
    count=0
    while n>0:
        num = n%10
        if digi ==num:
            count+=1
        n//=10
    return count



print(countocu(8976654545,6))
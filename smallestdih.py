#smalldih

def smalldih(n):
    n=abs(n)
    small=n%10
    n//=10
    while n>0:
        if small==0:
            return 0
        digi=n%10
        small=min(small,digi)
        n//=10
    return small

print(smalldih(5296))
print(smalldih(40345))
print(smalldih(-3454))

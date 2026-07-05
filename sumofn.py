#sumofn 

def sumofn(n):
   total=0
   while n>0:
      total+=n%10
      n//=10
   return total

print(sumofn(567))



#45%10 akaaa 45/10=4.5  remainder 5 is extracted 
#45//10 (whole division )meaning 45/10 = 4.5 only 4 remains as the fractinal part gets removed 

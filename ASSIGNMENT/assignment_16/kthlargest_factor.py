n=int(input())
k=int(input())
factor=0
for i in range(n):
    divisor=n-i
    if(n%divisor==0):
        factor=divisor  
        k-=1 
        if k==0:
            break 
print(factor)
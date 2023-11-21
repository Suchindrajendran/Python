m=int(input())
n=int(input())
if m>n:
    smallest=n 
else:
    smallest=m 
gcd=1
for i in range(1,smallest+1):
    if((m%i)==0) and ((n%i)==0):
        gcd=i
print(gcd)
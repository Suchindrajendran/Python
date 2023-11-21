m=int(input())
n=int(input())
if m>n:
    greatest=m 
else:
    greatest=n 
lcm_found=False
for i in range(greatest,(m*n+1)):
    if not(lcm_found):
        if((i%m)==0) and ((i%n)==0):
            lcm_found=True
            lcm=i 
print(lcm)
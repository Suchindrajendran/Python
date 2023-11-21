n=int(input())
sum=0
for i in range(1,n+1):
    num=int(input())
    factors=0
    for j in range(1,num+1):
        if(num%j==0):
            factors+=1 
    if(factors==2):
        sum+=num 
print(sum)
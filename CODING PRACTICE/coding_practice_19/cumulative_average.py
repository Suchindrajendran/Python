n=int(input())
sum=0
for i in range(1,n+1):
    num=int(input())
    sum+=num 
    result=sum/i 
    result=round(result,3)
    print(result)
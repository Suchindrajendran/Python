n=int(input())
s=float(input())
sum=0

for i in range(n):
    num=float(input())
    sum+=num 
sum=round(sum,3)
result=sum==s 
print(result)
x=float(input())
n=int(input())
sum=0
for i in range(1,n+1):
    term=x**i 
    sum+=term
sum=round(sum,4)
print(sum)
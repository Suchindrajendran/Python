n=int(input())
for i in range(n):
    num=int(input())
    factor=0
    for j in range(1,num+1):
        if(num%j==0):
            factor+=1 
    if(factor==2):
        print(num)
        break
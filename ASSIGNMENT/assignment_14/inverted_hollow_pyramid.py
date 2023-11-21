s=int(input())
n=int(input())
m=2*n 
for i in range(1,n+1):
    left_space=" "*(i-1)
    hollow_space="  "*(n-i-1)
    if i==1:
        row=""
        for j in range(1,n+1):
            row+=(str(s)+" ")
            s+=1
        print(row)
        last=s 
    elif(i<n):
        first=last 
        last=first
        for k in range(i,n):
            last+=1 
        row=left_space+(str(first)+" ")+hollow_space+(str(last)+" ")
        last+=1 
        print(row)
    else:
        row=left_space+str(last)
        print(row)
        
        
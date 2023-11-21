s=int(input())
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        s+=1
s-=1 
for i in range(1,n+1):
    left_space="  "*(i-1)
    hollow_space="  "*(n-i-1)
    if(i==1):
        row=""
        for j in range(1,n+1):
            row+=str(s)+" "
            s-=1
        print(row)
        last=s 
    elif(i<n):
        first=last
        last=first
        for k in range(i,n):
            last-=1 
        row=left_space+(str(first)+" ")+hollow_space+(str(last)+" ")
        print(row)
        last-=1
    else:
        row=left_space+hollow_space+str(last)+" "
        print(row)
        
        
        
        
    
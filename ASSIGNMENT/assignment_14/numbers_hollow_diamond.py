n=int(input())
m=2*n
for i in range(1,m):
    if(i<=n):
        left_space=" "*(n-i)
        hollow_space="  "*(i-2)
        if(i==1):
            row=left_space+"1 "
            last=1 
        else:
            row=""
            last+=1 
            row+=left_space+"1 "+hollow_space+(str(last)+" ")
        print(row)
        
    else:
        last=last-1
        left_space=" "*(i-n)
        hollow_space="  "*(m-i-2)
        if(i<(m-1)):
            row=left_space+"1 "+hollow_space+str(last)+" "
            print(row)
        else:
            row=left_space+"1 "
            print(row)
    
            
        
            
    
    
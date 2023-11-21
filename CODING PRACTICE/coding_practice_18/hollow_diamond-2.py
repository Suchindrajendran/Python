n=int(input())
m=2*n 
alpha_value=65

for i in range(1,m):
    if i==1:
        alpha=chr(alpha_value) 
        left_space=" "*(n-i)
        row=left_space+alpha
        print(row)
    elif i<=n:
        left_space=" "*(n-i)
        hollow_space="  "*(i-2)
        alpha_value+=1
        alpha=chr(alpha_value)+" "
        row=left_space+alpha+hollow_space+alpha
        print(row)
    elif i<m-1:
        left_space=" "*(i-n)
        alpha_value-=1 
        alpha=chr(alpha_value)+" "
        hollow_space="  "*(m-i-2)
        row=left_space+alpha+hollow_space+alpha
        print(row)
    else:
        left_space=" "*(i-n)
        alpha_value-=1 
        alpha=chr(alpha_value)
        row=left_space+alpha 
        print(row)
        
        
    
n=int(input())
alpha_value=65
for i in range(1,n+1):
    if i==1:
        alpha=chr(alpha_value)+" "
        left_space=" "*(n-i)
        right_space=left_space
        row=left_space+alpha+right_space
        result=row+row
        print(result)
    else:
        left_space=" "*(n-i)
        alpha_value+=1 
        alpha=chr(alpha_value)+" "
        hollow_space="  "*(i-2)
        right_space=left_space
        row=left_space+alpha+hollow_space+alpha+right_space
        result=row+row
        print(result)
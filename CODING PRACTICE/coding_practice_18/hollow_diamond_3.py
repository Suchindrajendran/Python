n=int(input())
m=2*n 
for i in range(1,m+1):
    star="* "
    if i<=n:
        star=star*(n-i+1)
        hollow_space="  "*(2*i-2)
        row=star+hollow_space+star 
        result=row
        print(result)
    else:
        star=star*(i-n)
        hollow_space="  "*(m-(2*(i-n)))
        row=star+hollow_space+star 
        result=row
        print(result)
        
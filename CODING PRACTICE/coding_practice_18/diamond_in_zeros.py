n=int(input())
m=2*n 

for i in range(1,m):
    zero="0 "
    dot=". "
    if(i==1 or i==(m-1)):
        dot=dot*(n-1)
        row=dot+zero+dot
        print(row)
    elif i<=n:
        dot=dot*(n-i)
        zero=zero*(2*i-1)
        row=dot+zero+dot
        print(row)
    else:
        dot=dot*(i-n)
        zero=zero*((m-2*(i-n))-1)
        row=dot+zero+dot
        print(row)
n=int(input())
pipe="|"
backward_slash="\\"
forward_slash="/"
m=2*n 
for i in range(1,m+1):
    if(i<=n):
        if i==1:
            row=pipe
            print(row)
        else:
            hollow_space=" "*(i-1)
            row=pipe+hollow_space+backward_slash
            print(row)
    else:
        if i<m:
            hollow_space=" "*(m-i)
            row=pipe+hollow_space+forward_slash
            print(row)
        else:
            row=pipe
            print(row)
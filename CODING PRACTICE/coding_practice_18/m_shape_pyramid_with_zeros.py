n=int(input())
for i in range(1,n+1):
    zeros="0 "*(2*i-1)
    dots=". "*(n-i)
    row=dots+zeros+dots
    result=row+row
    print(result)
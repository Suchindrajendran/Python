n=int(input())
smallest=999999999
for i in range(n):
    num=int(input())
    if(num<smallest):
        smallest=num 
    print(smallest)

m=int(input())
n=int(input())
if not(m>1):
    m=2
for i in range(m,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        result=i
        break
if is_prime:
    print(result)
else:
    print("No prime numbers in the given range")
        

    
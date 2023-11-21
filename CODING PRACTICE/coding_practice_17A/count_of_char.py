string=input()
n=int(input())
count=0
for i in string:
    unicode_value=ord(i)
    if(unicode_value==n):
        count+=1 
print(count)
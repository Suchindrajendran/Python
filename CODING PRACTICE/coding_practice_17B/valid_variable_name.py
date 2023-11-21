s=input()
for char in s:
    i=ord(char)
    if((i>=65)and(i<=90)) or ((i>=97)and(i<=122)) or ((i>=48)and(i<=57)):
        is_valid=True 
    else:
        is_valid=False
        break
print(is_valid)
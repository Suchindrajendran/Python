string=input()
result=""
for i in string:
    unicode_value=ord(i)
    new_value=unicode_value+1 
    new_char=chr(new_value)
    print(new_char)
    
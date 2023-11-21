string=input()
length=len(string)
smallest=string[0]
smallest_value=ord(smallest)
for i in range(1,length):
    char=string[i]
    unicode_value=ord(char)
    if(unicode_value<smallest_value):
        smallest_value=unicode_value
smallest_letter=chr(smallest_value)
print(smallest_letter)
    
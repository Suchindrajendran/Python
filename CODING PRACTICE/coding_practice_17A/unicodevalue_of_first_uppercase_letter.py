string=input()
for i in string:
    if i.isupper():
        unicode_value=ord(i)
        break
print(unicode_value)
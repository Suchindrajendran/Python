string=input()
result=""
for each_char in string:
    if each_char.isupper():
        result+=each_char
        break
print(result)
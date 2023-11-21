string=input()
length=len(string)
last_char=string[len(string)-1]
comma=","
new_string=""
for i in range(length-1):
    char=string[i]
    new_char=char+comma 
    new_string+=new_char
new_string+=last_char
print(new_string)
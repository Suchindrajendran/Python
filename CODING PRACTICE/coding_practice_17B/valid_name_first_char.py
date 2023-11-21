s=input()
first_char=s[0]
unicode_value=ord(first_char)

is_upper=(unicode_value>=65 and unicode_value<=90)
is_lower= unicode_value>=97 and unicode_value<=122
is_underscore=first_char=="_"

if(is_upper or is_lower or is_underscore):
    is_valid=True
else:
    is_valid=False
print(is_valid)
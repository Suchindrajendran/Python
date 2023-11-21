string=input()
substring=input()
substring_index=0 
substring_length=len(substring)
for char in string:
    if char==substring[substring_index]:
        substring_index+=1 
        if substring_index==substring_length:
            break
if (substring_index==substring_length):
    print("Yes")
else:
    print("No")

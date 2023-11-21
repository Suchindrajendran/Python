numbers=input()
number_list=numbers.split()
length=len(number_list)
for num in range(length):
    number_list[num]=int(number_list[num])
if(length%2==0):
    first_half=number_list[:int(length/2)]
if(length%2==1):
    first_half=number_list[:int(length/2)+1]
print(first_half)
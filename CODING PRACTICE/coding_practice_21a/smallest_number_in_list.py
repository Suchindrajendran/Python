numbers=input()
numbers_list=numbers.split()
smallest_num=int(numbers_list[0])
for num in numbers_list:
    num=int(num)
    if(num<smallest_num):
        smallest_num=num 
print(smallest_num)
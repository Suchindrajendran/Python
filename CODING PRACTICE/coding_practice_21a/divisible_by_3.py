numbers=input()
numbers_list=numbers.split()
resultant_list=[]
for num in numbers_list:
    num=int(num)
    if(num%3==0):
        resultant_list+=[num]
print(resultant_list)
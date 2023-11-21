sentence=input()
new_sentence=sentence.split()
result=""

for i in new_sentence:
    if(len(i)>2):
        char=i[2]
        result+=char
result_list=",".join(result)
print(result_list)
    
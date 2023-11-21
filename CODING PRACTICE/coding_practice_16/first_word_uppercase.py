string=input()
result=""
length=len(string)
for i in range(length):
    each_char=string[i]
    if each_char==" ":
        break 
first_word=string[:i]
first_word=first_word.upper()
final_word=string[i:]
word=first_word+final_word
print(word)
    
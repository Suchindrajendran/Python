s=input()
first_word=s
word=""
length=len(s)
for i in range(length):
    char=s[i]
    word+=char
    if char==" " or i==len(s)-1:
        if(word.lower()<first_word.lower()):
            first_word=word
        word=""
print(first_word)
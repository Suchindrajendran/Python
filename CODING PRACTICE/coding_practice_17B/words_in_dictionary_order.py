s=input()
length=len(s)
firstword="z"
lastword="a"
word=""
for i in range(length):
    char=s[i]
    if(char!=" "):
        word+=char
    if(char==" " or i==length-1):
        if(word.lower() < firstword.lower()):
            firstword=word 
        if( word.lower() > lastword.lower()):
            lastword=word 
        word=""
result=firstword+" "+lastword
print(result)

sentence=input()
sentence_list=sentence.split()
for word in sentence_list:
    firt_letter=word[0]
    last_letter=word[len(word)-1]
    result=firt_letter.lower()==last_letter.lower()
    print(result)
        
        
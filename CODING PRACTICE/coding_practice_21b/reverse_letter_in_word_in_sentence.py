sentence=input()
sentence_list=sentence.split()
resultant_sentence=[]
for word in sentence_list:
    reversed_word=word[::-1]
    resultant_sentence+=[reversed_word]
resultant_sentence=" ".join(resultant_sentence)
print(resultant_sentence)
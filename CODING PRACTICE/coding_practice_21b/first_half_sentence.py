sentence=input()
sentence_list=sentence.split()
length=len(sentence_list)

if(length%2==0):
    first_half_sentence=sentence_list[:int(len(sentence_list)/2)]
if(length%2==1):
    first_half_sentence=sentence_list[:int(len(sentence_list)/2)+1]

print(first_half_sentence)
sentence=input().split()
n=int(input())
length=len(sentence)
new_sentence=sentence[length:-n-1:-1]
print(new_sentence)
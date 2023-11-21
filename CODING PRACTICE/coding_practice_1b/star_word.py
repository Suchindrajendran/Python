a=3
lista=[1,2]
listb=lista+[a]
print(id(lista)==id(listb))
lista+=[4]
print(listb)
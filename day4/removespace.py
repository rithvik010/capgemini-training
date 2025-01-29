sentence=input("enter a sentance")
print(sentence)
c=0
for char in sentence:
    i=sentence.find(char)
   # if i<len(sentence)-1:
    if char==" ":
        c+=1
        next_letter=sentence[i+1]
        if next_letter==" ":
            new_sentence=sentence.replace(next_letter,'')
print(new_sentence)

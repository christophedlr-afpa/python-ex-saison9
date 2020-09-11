sentence = ""
leftSentence = ""
rightSentence = ""
charpos: int

print("Veuillez entrer une phrase : ")
sentence = input()
charpos = int(input("Indiquez la position d'un caractère de la chaîne, ce dernier sera supprimé : "))

leftSentence = sentence[0:charpos]
rightSentence = sentence[charpos+1:len(sentence)-1]
sentence = leftSentence+rightSentence

print("La nouvelle phrase : ")
print(sentence)

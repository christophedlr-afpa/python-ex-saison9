sentence = ""

print("Indiquez une phrase")
sentence = input(" ")

print("Codification de votre phrase")

for i in range(0, len(sentence)-1):
    sentence = sentence[0:i]+chr(ord(sentence[i:i+1])+1)+sentence[i+1:len(sentence)]

print("Votre phrase codée :")
print(sentence)

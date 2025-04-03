#Sawyer Wood, ProficiencyTest Secret Sypher.
word = input("What is the word you want to Cipher/Decipher?: ")
idk = input("Do you want to cipherify or decipherify?: ")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1"]
shiftedalphabet = ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", ":", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "1"]

def Cipherify(word):
    wordspot = 0
    alphabetspot = 0
    stopoint = len(word)
    while wordspot < stopoint:
        if word[wordspot] == alphabet[alphabetspot]:
            letter = shiftedalphabet[alphabetspot]
            wordspot = wordspot + 1
            alphabetspot = 0
            print(letter)
        else:
            alphabetspot = alphabetspot + 1

def Decipherify(word):
    wordspot = 0
    alphabetspot = 0
    stopoint = len(word)

    while wordspot < stopoint:
        if word[wordspot] == shiftedalphabet[alphabetspot]:
            letter = alphabet[alphabetspot]
            wordspot = wordspot + 1
            alphabetspot = 0
            print( letter)
        else:
            alphabetspot = alphabetspot + 1

if idk == str("cipher"):
    Cipherify(word)
elif idk == str("decipher"):
    Decipherify(word)
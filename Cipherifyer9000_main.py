#Sawyer Wood, ProficiencyTest Secret Sypher.
def main():
    idk = input("\nDo you want to 1. Cipher, 2. Decipher?: ")

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1"]
    shiftedalphabet = ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", ":", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "1"]

    def Cipherify(word):
        cipheredword = ""
        wordspot = 0
        alphabetspot = 0
        stopoint = len(word)
        while wordspot < stopoint:
            if word[wordspot] == alphabet[alphabetspot]:
                letter = shiftedalphabet[alphabetspot]
                wordspot = wordspot + 1
                alphabetspot = 0
                cipheredword = cipheredword + letter
            else:
                alphabetspot = alphabetspot + 1
        print(f"\n{cipheredword}")

    def Decipherify(word):
        decipheredword = ""
        wordspot = 0
        alphabetspot = 0
        stopoint = len(word)

        while wordspot < stopoint:
            if word[wordspot] == shiftedalphabet[alphabetspot]:
                letter = alphabet[alphabetspot]
                wordspot = wordspot + 1
                alphabetspot = 0
                decipheredword = decipheredword + letter
            else:
                alphabetspot = alphabetspot + 1
        print(f"\n{decipheredword}")

    if idk == str("1"):
        word = input("\nWhat is the word you want to cipher?: ")
        Cipherify(word)
    elif idk == str("2"):
        word = input("\nWhat is the word you want to decipher?: ")
        Decipherify(word)
    else:
        print("\nInvalid input. Please try again.")
        main()
    return
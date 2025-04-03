#Sawyer Wood, random password generator

#Importing random library and string library
import random

#Required lists for creating the password
LowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

#Exception handling for ints
def intchecker(Inputx):
    try:
        Inputx = int(Inputx)
        return(Inputx)
    except:
        print("\nThat is not a valid input.")
        return None

#Exception handling for yes or no
def yesnointchecker(Inputx):
    if Inputx in ["1", "2"]:
        return(Inputx)
    else:
        print("\nThat is not a valid input.")
        return None

def generatepasswordparameters():
    Listtopickfrom = []
    #Asking for the paramiters for the password and checking that they are the correct inputs
    LenOPassword = intchecker(input("\nHow long do you want the password to be? \t"))
    if type(LenOPassword) == int:
        IncludeLowercase = yesnointchecker(input("\nDo you want to include lowercase letters? 1: Yes. 2: No\t"))
        if IncludeLowercase != None:
            IncludeUppercase = yesnointchecker(input("\nDo you want to include uppercase letters? 1: Yes. 2: No\t"))
            if IncludeUppercase != None:
                IncludeNumbers = yesnointchecker(input("\nDo you want to include numbers? 1: Yes. 2: No\t"))
                if IncludeNumbers != None:
                    IncludeSymbols = yesnointchecker(input("\nDo you want to include special characters? 1: Yes. 2: No\t"))
                    if IncludeSymbols != None:
                        #Setting what the passwords can contain
                        if IncludeLowercase == "1":
                            Listtopickfrom.append(LowercaseLetters)
                        if IncludeUppercase == "1":
                            Listtopickfrom.append(UppercaseLetters)
                        if IncludeNumbers == "1":
                            Listtopickfrom.append(Numbers)
                        if IncludeSymbols == "1":
                            Listtopickfrom.append(Symbols)
                        if [IncludeLowercase, IncludeUppercase, IncludeNumbers, IncludeSymbols] == ["2", "2", "2", "2"]:
                            print("\nYou said no to all of the options, try again.")
                        else:
                            generatepassword(LenOPassword, Listtopickfrom)

def generatepassword(LenOPassword, Listtopickfrom):
    #Making the 4 passwords
    for y in range(4):
        Password = ""
        for x in range(LenOPassword):
            randomlist = random.choice(Listtopickfrom)
            Password = Password + random.choice(randomlist)
        print("\n", Password)


def main():
    #Choice between generate password and quit
    choice = input("\nWhat do you want to do? 1: Generate Password, 2: Quit\t")

    if choice == "1":
        generatepasswordparameters()
    elif choice == "2":
        return
    else:
        print("\nThat is not a valid input.")

#Clearing Screen
print("\033[H\033[J")
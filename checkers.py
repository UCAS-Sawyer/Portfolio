#Sawyer Wood, file with functions that check stuff

#Exception handling for ints
def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)

        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input. Not an int")
        return None

#Checker for names
def name_checker(name, characters):

    #Checking if the name is taken
    for player in characters:
        if player["name"] == name:
            print("\nThat name is already taken, please try again.")
            name = input("\nPlease enter the name of your character.\n")
            name_checker(name, characters)
        else:
            return name
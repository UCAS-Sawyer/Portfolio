#Sawyer Wood, Battle Simulator character creator main

from character_creator import player_list_creator
from character_creator import character_creator

#The main for the caracter creation
def character_creation_main():
    choice = input("\nDo you want to continue to create a character, 1. Yes, 2. No ?\n")
    if choice == "1":
        characters = player_list_creator()
        character_creator(characters)
    elif choice == "2":
        return
    else:
        print("\nThat is not an option.")
        character_creation_main()
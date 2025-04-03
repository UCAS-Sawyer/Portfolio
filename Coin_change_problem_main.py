#Sawyer Wood Coin Changer problem main

from Coin_Change_Problem import coin_change_main

#This is the main function
def main():
    choice = input("\nWhat would you like to do, 1: Continue to Coin Change Problem, 2: Exit?\n")

    if choice == "1":
        coin_change_main()
    elif choice == "2":
        return
    else:
        print("\nThat is not an option.")
    
    main()
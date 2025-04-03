# Sawyer Wood, Portfolio main

import sys
import os
import time

# Importing main functions from different modules
from Coin_change_problem_main import main as coin_change_main
from BattleSimulator_main import main as battle_simulator_main
from ShortestDoungeonCrawlerEvermain import main as shortest_dungeon_crawler_main
from RandomPasswordGenratormain import main as random_password_generator_main
from ToDoList_main import main as to_do_list_main
from ToDoList_main import number_of_lines as number_of_lines
from Cipherifyer9000_main import main as cipherifyer9000_main

def main():
    # Display the menu options
    print("\nPlease choose an option:\n1. Coin Change Problem\n2. Battle Simulator\n3. Shortest Dungeon Crawler Ever\n4. Random Password Generator\n5. To-Do List\n6. Cipherifyer9000\n7. Exit")
    choice = input("Enter your choice (1-7): ")

    # Checking input
    if choice == '1':
        time.sleep(1)
        coin_change_main()
    elif choice == '2':
        time.sleep(1)
        battle_simulator_main()
    elif choice == '3':
        time.sleep(1)
        shortest_dungeon_crawler_main()
    elif choice == '4':
        time.sleep(1)
        random_password_generator_main()
    elif choice == '5':
        time.sleep(1)
        number_lines = number_of_lines()
        to_do_list_main(number_lines)
    elif choice == '6':
        time.sleep(1)
        cipherifyer9000_main()
    elif choice == '7':
        print("\nExiting the Portfolio. Goodbye!")
        sys.exit()  # Exit the program
    else:
        print("\nInvalid choice. Please try again.")
    
    main()

# Welcome message
print("\nWelcome to the Portfolio!")
# Clear the console screen
os.system('cls' if os.name == 'nt' else 'clear')

# Start the main function
main()
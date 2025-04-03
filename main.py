# Sawyer Wood, Portfolio main

import sys
import os

# Importing main functions from different modules
from Coin_change_problem_main import main as coin_change_main
from BattleSimulator_main import main as battle_simulator_main
from ShortestDoungeonCrawlerEvermain import main as shortest_dungeon_crawler_main
from RandomPasswordGenratormain import main as random_password_generator_main
from ToDoList_main import main as to_do_list_main
from ToDoList_main import number_of_lines as number_of_lines

def main():
    # Display the menu options
    print("\nPlease choose an option:\n1. Coin Change Problem\n2. Battle Simulator\n3. Shortest Dungeon Crawler Ever\n4. Random Password Generator\n5. To-Do List\n6. Exit")
    choice = input("Enter your choice (1-6): ")

    # Checking input
    if choice == '1':
        coin_change_main()
    elif choice == '2':
        battle_simulator_main()
    elif choice == '3':
        shortest_dungeon_crawler_main()
    elif choice == '4':
        random_password_generator_main()
    elif choice == '5':
        number_lines = number_of_lines()
        to_do_list_main(number_lines)
    elif choice == '6':
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
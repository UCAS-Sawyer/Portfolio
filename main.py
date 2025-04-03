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
        print("\nThis project solves the Coin Change Problem. It was very fun to do and I learned a lot. I learned more on how to use csvs.")
        time.sleep(4)
        coin_change_main()

    elif choice == '2':
        print("\nThis project allows you to create characters, fight with characters and level them up, and see theirs stats with the use of different charts. I liked this project, even though it was hard a times. I learned a lot on how to use some python libraries.")
        time.sleep(4)
        battle_simulator_main()

    elif choice == '3':
        print("\nThis project was one of my finals. It is a little adventuer/dungeon crawler game. It was very fun to do and it really was a test of my skills. It helped me to develope my general probelm solving and programing skills.")
        time.sleep(4)
        shortest_dungeon_crawler_main()

    elif choice == '4':
        print("\nThis project creates a password with some conditions it is given. This one I made earlier in my programming life, so I didn't know much. I learned lots on conditionals and the like.")
        time.sleep(4)
        random_password_generator_main()

    elif choice == '5':
        print("\nThis project counts the number of words in a txt file that you give it. This one was a challenge for me, because I was just learning how to use fiels. It expounded my knowledge of using files.")
        time.sleep(4)
        number_lines = number_of_lines()
        to_do_list_main(number_lines)

    elif choice == '6':
        print("\nThis project uses a ceaser cipher on anyword you give it. It can encode a word or decode it if it used the same ceaser cipher. It was very fun to do and I learned a lot about lists and for loops.")
        time.sleep(4)
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
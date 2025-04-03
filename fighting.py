#Sawyer Wood, Battle Simulator fighting and battle sim

import csv
import random
import time
import math
import pandas as pd
from faker import Faker
fake= Faker()

from character_creator import player_list_creator
from checkers import intchecker

#The main for the fighting
def fighting_main():
    choice = input("\nDo you want to continue to battle, 1. Yes, 2. No ?\n")
    if choice == "1":
        characters = player_list_creator()
        battle_character(characters)
        fighting_main()
        return
    elif choice == "2":
        return
    else:
        print("\nThat is not an option.")
        fighting_main()

def monster_list_creator(file_path):
    #List of all the characters
    monsters = []

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            #Creating the dictionary

            monster = {
                "name" : row[0],
                "health" : int(row[1]),
                "strength" : int(row[2]),
                "defense" : int(row[3]),
                "speed" : int(row[4]),
                "xp" : int(row[5])
            }
            monsters.append(monster)

        return monsters

#choosing the character
def battle_character(characters):
    print("\nWhich character do you want to use?")
    character_number = 0

    #Printing all the characters
    # Load the entire CSV
    character_csv = pd.read_csv('csvs/characters.csv')

    # Display the DataFrame
    print(character_csv)

    #Choosing the character and error handling
    character_choice = intchecker(input("\nEnter the number of the character: "))

    if character_choice != None:
        if 0 <= character_choice and character_choice <= character_number:

            chosen_character = characters[character_choice]
            print(f'\nYou have chosen, {chosen_character["name"]}, to fight with.')
            battle(chosen_character,character_choice)
            return
        else:
            print("\nThat character number does not exist, try again.")
            return
    else:
        return
    
def battle(chosen_character,character_number):
    #Setting the monsters according to the character lvl
    if chosen_character["level"] >=0 and chosen_character["level"] <= 3:
        monsters = monster_list_creator("csvs/easy_monsters.csv")
    elif chosen_character["level"] >3 and chosen_character["level"] <= 8:
        monsters = monster_list_creator("csvs/medium_monsters.csv")
    else:
        monsters = monster_list_creator("csvs/hard_monsters.csv")

    def update_character():
        #writing the characters new stats to csv
        with open("csvs/characters.csv", "r") as file:
            lines = list(csv.reader(file))

        with open("csvs/characters.csv", "w", newline='') as file:
            writer = csv.writer(file)
            lines[character_number + 1] = chosen_character["name"],chosen_character["health"],chosen_character["strength"],chosen_character["defense"],chosen_character["speed"],chosen_character["level"],chosen_character["xp"],chosen_character["description"]
            writer.writerows("")
            writer.writerows(lines)
            return

    #Doing lvl up stuff
    def monster_dead():
        nonlocal chosen_character, monster

        bad_adj = ["angry", "arrogant", "bitter", "careless", "clumsy", "cruel", "deceitful", "defiant", "fearful", "greedy", "grumpy", "harsh", "ignorant", "impatient", "insecure", "lazy", "malicious", "narrow-minded", "pessimistic", "rude", "selfish", "stubborn", "tactless", "unreliable", "vindictive"]

        #Faker is used to create a victory phrase
        print(f"\nI, the {fake.catch_phrase()} man has killed this {fake.random_element(bad_adj)} {monster['name']}!")

        #Give the character xp
        new_xp = chosen_character["xp"] + monster["xp"]
        lvlup_stat_change = None

        #If the character has enough xp to level up they level up and gain a stat
        if new_xp >= chosen_character["level"] * 15:
            stats = ["health","strength","defense","speed"]
            
            new_xp -= chosen_character["level"] * 15
            chosen_character["level"] += 1

            lvlup_stat_change = random.choice(stats)
            chosen_character[lvlup_stat_change] += 2

            time.sleep(0.7)
            print(f"\nYou have leveled up! {lvlup_stat_change} is now {chosen_character[lvlup_stat_change]}.")
            time.sleep(0.7)
            print(f"\nYou have defeated the {monster['name']} and have gained {monster['xp']} xp, so you are now Level: {chosen_character['level']} and have {new_xp} xp.")

        return lvlup_stat_change, new_xp, chosen_character["level"]
    
    #Picking which monster to fight
    monster = random.choice(monsters)
    print(f"\nYou are going to fight a {monster['name']}.")

    #Setting current health to base health
    character_health = chosen_character["health"]

    #Deciding who goes first
    if chosen_character["speed"] > monster["speed"]:
        time.sleep(0.7)
        print("\nYou get to go first.")

        #While the monster is still alive
        while monster["health"] > 0:
            monster["health"] -= chosen_character["strength"] + 2
            time.sleep(0.7)
            print(f"\nYou attack the {monster['name']} and do {chosen_character['strength'] + 2} dmg to the {monster['name']}.")
            
            #If the monster is dead do lvl stuffffff
            if monster["health"] <= 0:
                lvlup_stat_change, xp, level = monster_dead()
                if chosen_character["level"] == level:
                    chosen_character["xp"] = xp
                    print(f"\nYou have defeated the {monster['name']} and have gained {monster['xp']} xp, so you are now Level: {chosen_character['level']} and have {chosen_character['xp']} xp.")
                else:
                    #Setting the stats to their new values
                    chosen_character["xp"] = xp
                    chosen_character["level"] = level
                update_character()
                return
            
            else:
                time.sleep(0.7)
                print(f"\nThat hit did not kill the {monster['name']}.")
            
            #Monster attacks
            character_health -= math.floor(monster["strength"]/(chosen_character["defense"]/2))
            time.sleep(0.7)
            print(f"\nThe {monster['name']} attacks {chosen_character['name']} and does {math.floor(monster['strength']/(chosen_character['defense']/2))} dmg to {chosen_character['name']}. {chosen_character['name']} has {character_health} hp left.")

            if character_health <= 0:
                print(f"\n{chosen_character['name']} has died.")
                return
            else:
                pass

    else:
        time.sleep(0.7)
        print(f"\nThe {monster['name']} gets to go first.")

        #While the monster is still alive
        while monster["health"] > 0:
            #Monster attacks
            character_health -= math.floor(monster["strength"]/(chosen_character["defense"]/2))
            time.sleep(0.7)
            print(f"\nThe {monster['name']} attacks {chosen_character['name']} and does {math.floor(monster['strength']/(chosen_character['defense']/2))} dmg to {chosen_character['name']}. {chosen_character['name']} has {character_health} hp left.")

            if character_health <= 0:
                print(f"\n{chosen_character['name']} has died.")
                return
            else:
                pass

            monster["health"] -= chosen_character["strength"] + 2
            time.sleep(0.7)
            print(f"\nYou attack the {monster['name']} and do {chosen_character['strength'] + 2} dmg to the {monster['name']}.")

            #If the monster is dead do lvl stuffffff
            if monster["health"] <= 0:
                lvlup_stat_change, xp, level = monster_dead()
                if chosen_character["level"] == level:
                    chosen_character["xp"] = xp
                    print(f"\nYou have defeated the {monster['name']} and have gained {monster['xp']} xp, so you are now Level: {chosen_character['level']} and have {chosen_character['xp']} xp.")
                else:
                    #Setting the stats to their new values
                    chosen_character["xp"] = xp
                    chosen_character["level"] = level
                update_character()
                return
            
            else:
                time.sleep(0.7)
                print(f"\nThat hit did not kill the {monster['name']}.")
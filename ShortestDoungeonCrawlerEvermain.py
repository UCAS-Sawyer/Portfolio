#Sawyer Wood, Final

import os
import time

PlayerGold = 20
Inventory = ["Shortsword", "Health Potion"]
PlayerHealth = 25
PlayerSpeed = 10
PlayerStrenght = 3

Timeloop = 0

Restcount = 0
WaterCollected = "No"
BeenToRoom2 = "No"
BeenToRoom3 = "No"
ChestOpen4 = "No"
BeenToRoom5 = "No"
ChestOpen6 = "No"


Room3Monster = {
    "Attack" : 3,
    "Health" : 10,
    "Speed" : 9,
    "Reward" : 15,
    "Monster name" : "Skeleton"
}

Boss = {
    "Attack" : 5,
    "Health" : 30,
    "Speed" : 11,
    "Reward" : 50,
    "Monster name" : "Necromancer"
}
def main():
    def TownCenter():
        print ("\nYou can go to the Shop, the House, the River, or the Dungeon.")
        TownCenterDirection = input("\nWhere do you want to go?(Shop, House, River, Dungeon)\t")
        TownCenterDirection = TownCenterDirection.lower()

        if TownCenterDirection in ["shop", "house", "river", "dungeon", "stop"]:
            if TownCenterDirection == "shop":
                Shop()
            if TownCenterDirection == "house":
                House()
            if TownCenterDirection == "river":
                River()
            if TownCenterDirection == "dungeon":
                DungeonEntrance()
            if TownCenterDirection == "stop":
                print("\nThe End")
                return
        else:
            print("\nThat is not an option")
            TownCenter()

    def Shop():
        global PlayerGold, PlayerSpeed

        ShopInventory = ["Health potions: 10g", "Speed potions: 15g", "Longsword: 30g"]
        print(f"\nYou enter the old shop and see all the wares on the walls and counters. Welcome worrior we have: {ShopInventory}")
        print(f"\nYou have {PlayerGold} gold.")
        while True:
            DoYouWantToBuy = input("\nWould you like to buy something?(Yes or No)\t")
            DoYouWantToBuy = DoYouWantToBuy.lower()

            if DoYouWantToBuy == "no":
                print("\nYou leave the shop and go back into the town center")
                TownCenter()
                break
            elif DoYouWantToBuy == "yes":
                WhatDoYouWantToBuy = input("\nWhat would you like to buy?\t")
                WhatDoYouWantToBuy = WhatDoYouWantToBuy.lower()

                if WhatDoYouWantToBuy == "health potion" and PlayerGold >= 10:
                    print("\nYou baught a health potion.")
                    PlayerGold -= 10
                    Inventory.append("Health Potion")
                elif WhatDoYouWantToBuy == "speed potion" and PlayerGold >=15:
                    print("\nYou baught a speed potion and you drink it.(+1 Speed)")
                    PlayerGold -= 15
                    PlayerSpeed += 1
                elif WhatDoYouWantToBuy == "longsword" and PlayerGold >= 30:
                    print("\nYou bought a longsword")
                    PlayerGold -= 30
                    Inventory.insert(0, "Longsword")
                    print("\nYou will automatically use this weapon in combat since it is your best one.")
                else:
                    print("\nYou do not have enough money or you spelled it wrong.")
                
                print(f"\nYour inventory contains {Inventory} and you have {PlayerGold} gold")

    def House():
        global PlayerHealth, Restcount

        print("\nYou walk up the cobblestone pathway to your house. You enter your house and climb the stairs to your room.")
        Rest = input("\nDo you want to rest?(Yes/No)\t")
        Rest = Rest.lower()

        if Rest == "yes":
            Restcount += 1
            print("\nYou rest for a while.")

            if Restcount <= 5:
                PlayerHealth = PlayerHealth + 2
                print(f"\nYou are well rested(+2 health), your health is now {PlayerHealth} and ready for an adventure, so you go back to the town center.")

            elif Restcount > 5 and Restcount <= 6:
                PlayerHealth = PlayerHealth + 2
                print(f"\nYou are well rested(+2 health), your health is now {PlayerHealth}, so you go back to the town center.")

            elif Restcount > 6 and Restcount <= 7:
                PlayerHealth = PlayerHealth + 0
                print(f"\nYou go back to the town center!")

            elif Restcount == 8:
                PlayerHealth = PlayerHealth -2
                print(f"\nYour health is now {PlayerHealth}, you have rested too much!")

            elif Restcount == 9:
                PlayerHealth = 0
                print(f"\nYou shall never wake again, cheater!")
                print("\fAchievement found: Anger the Narrator.")
                NarratorBoss()

            TownCenter()
        else:
            print("\nYou decide you want to go back into the town center.")
            TownCenter()

    def River():
        global WaterCollected
        print("\nYou walk down the dirt pathway to the river. You hear the gushing of the water even before you see it. The path opens up to a river that is fast but fairly small.")

        if "Water" in Inventory:
            print("\nYou sit there for a while, but there is nothing for you to do here so you decide to leave and walk up the path back to the town center.")
            TownCenter()

        elif WaterCollected == "Yes":
            print("\nYou sit there for a while, but there is nothing for you to do here so you decide to leave and walk up the path back to the town center.")
            TownCenter()

        else:
            CollectWaterChoice = input("\nDo you want to collect water?\t")
            CollectWaterChoice = CollectWaterChoice.lower()

            if CollectWaterChoice == "yes":
                WaterCollected = "Yes"
                print("\nYou grab your extra flask and you fill it with the crystal clear water.(+Water)")
                Inventory.append("Water")

                print("\nYou enjoy the peace for a bit and then you go back to the town center.")
                TownCenter()
            else:
                print("\nYou stand there for a while, but you decide to head back to the town center.")
                TownCenter()

    def DungeonEntrance():
        EnterDungeon = input("\nDo you want to enter the dungeon?(Yes/No)\t")
        EnterDungeon = EnterDungeon.lower()

        if EnterDungeon == "yes":
            print("\nYou enter the crypt by descending down the long winding staircase.")
            Room1()
        else:
            print("\nYou decide that you aren't ready and you go back to the village.")
            TownCenter()

    def Room1():
        global Inventory
        print("\nYou enter a damp spacious room that has a big fountain in the middle. There is a plaque on the fountain that says ‘This fountain thirsts for the clear wine from the big river devine.")

        if "Water" in Inventory:
            PourWater = input("\nDo you want to pour the water into the fountain?(Yes/No)\t")
            PourWater = PourWater.lower()

            if PourWater == "yes":
                print("\nYou pour the crystal clear water into the fountain and nothing happens(-Water). Then you hear a bubbling noise as the fountain starts to run. You can now see there is an object at the bottom of the fountain. You reach into the water and you pull out a long sword.(+Longsword)")

                Inventory.remove("Water")
                Inventory.insert(0, "Longsword")
                print(f"\nYou will automatically use this weapon in combat since it is your best one. You have {Inventory} in your inventory.")

        print("\nYou can go to a chest room(Room 6), the coin room(Room 2), the combat(Room3), or go to town")
        Room1Direction = ""
        while Room1Direction not in ["room 2", "room 3", "room 6", "town"]:
            Room1Direction = input("\nWhere do you want to go?(Room 6, Room 2, Room 3, Town)\t")
            Room1Direction = Room1Direction.lower()

        if Room1Direction == "room 6":
            Room6()
        if Room1Direction == "room 2":
            Room2()
        if Room1Direction == "room 3":
            Room3()
        if Room1Direction == "town":
            TownCenter()


    def Room2():
        global PlayerGold
        global PlayerHealth
        global BeenToRoom2
        if BeenToRoom2 == "No":
            BeenToRoom2 = "Yes"
            print("\nYou enter a strange empty room with little slits all over the wall on infront of you. You hear some gears start to turn and then coins start shooting out of the slits and the far end of the room. You try to dive to the ground to dodge the coins.")

            if PlayerSpeed > 10:
                print("\nYou dive to the ground and dodge all of the coins. You collect the coins off the ground.(+10 gold)")

                PlayerGold += 10
                print(f"\nYou now have {PlayerGold} gold.")
            
            else:
                print("\nYou were too slow and you get hit by some of the coins and then they evaporate into thin air.(-5 health)")

                PlayerHealth -= 5
                IsPlayerDead()
                print(f"\nYou are hurt but you are still okay, your health is {PlayerHealth}.")

                if "Health Potion" in Inventory:
                        UseHealhtPotion = input("\nDo you want to use a health potion?(Yes/No)\t")
                        UseHealhtPotion = UseHealhtPotion.lower()

                        if UseHealhtPotion == "yes":
                            print("\nYou use a health potion.(+5 health, - health potion)")
                            PlayerHealth += 5

                            Inventory.remove("Health Potion")
                            print(f"\nYour health is now {PlayerHealth} and you have {Inventory} in your inventory.")
        print("\nYou can go to the fountain room(Room 1) or you can go to the chest room(Room 4)")
        Room2Direction = ""
        while Room2Direction not in ["room 1", "room 4"]:
            Room2Direction = input("\nWhere do you want to go?(Room 1, Room 4)\t")
            Room2Direction = Room2Direction.lower()

        if Room2Direction == "room 1":
            Room1()
        elif Room2Direction == "room 4":
            Room4()

    def Room3():
        global Room3Monster, BeenToRoom3
        if BeenToRoom3 == "No":
            BeenToRoom3 = "Yes"
            print("\nYou walk into the room and there is a pile of bones in the corner. You inspect them closer, then they come alive. Entering combat good luck.")
            Combat(Room3Monster)

            print("\nYou defeated the skeloton, now the room is empty.")
        print("\nYou can go to the fountain room(Room 1) or you can go to reward room(Room 5)")
        Room3Direction = ""
        while Room3Direction not in ["room 1", "room 5"]:
            Room3Direction = input("\nWhere do you want to go?(Room 1, Room 5)\t")
            Room3Direction = Room3Direction.lower()

        if Room3Direction == "room 1":
            Room1()
        elif Room3Direction == "room 5":
            Room5()

    def Room4():
        global ChestOpen4, PlayerHealth, PlayerGold
        
        print("\nYou want into a bare room, the only thing in the room is a chest.")
        if ChestOpen4 == "No":
            OpenChest = input("\nDo you want to open the chest?(Yes/No)\t")
            OpenChest = OpenChest.lower()

            if OpenChest == "yes":
                ChestOpen4 = "Yes"

                PlayerGold += 5
                PlayerHealth -= 2
                print("\nYou open the chest, but it is a trap! You gain 5 gold, but lose 2 health.")
                IsPlayerDead()
                print(f"\nYou now have {PlayerGold} gold and {PlayerHealth} health.")
        
        print("\nYou can go to the coin room(Room 2) or you can go to a chest room(Room 6)")
        Room4Direction = ""
        while Room4Direction not in ["room 2", "room 6"]:
            Room4Direction = input("\nWhere do you want to go?(Room 2, Room 6)\t")
            Room4Direction = Room4Direction.lower()

        if Room4Direction == "room 2":
            Room2()
        if Room4Direction == "room 6":
            Room6()
                
    def Room5():
        global PlayerHealth, PlayerGold, BeenToRoom5
        print("\nYou walk into a room with a mystical air to it.")
        if BeenToRoom5 == "No":
            BeenToRoom5 = "Yes"
            if PlayerHealth <=18:
                PlayerHealth += 10
                print(f"\nYou feel your wounds close. You have been healed(+10), your health is now {PlayerHealth}.")
            else: 
                PlayerGold += 5
                print(f"\nYou feel your gold pouch grow heavier. You have gained 5 gold, you now have {PlayerGold} gold.")
        
        print("\nYou can go to the combat room(Room 3) or you can go to a chest room(Room 6)")
        Room5Direction = ""
        while Room5Direction not in ["room 3", "room 6"]:
            Room5Direction = input("\nWhere do you want to go?(Room 3, Room 6)\t")
            Room5Direction = Room5Direction.lower()

        if Room5Direction == "room 3":
            Room3()
        if Room5Direction == "room 6":
            Room6()

    def Room6():
        global ChestOpen6, PlayerGold, PlayerHealth
        print("\nYou enter a room with a chest in the corner.")
        if ChestOpen6 == "No":
            ChestOpen6 = "Yes"
            OpenChest = input("\nDo you want to open the chest.(Yes/No)\t")
            OpenChest = OpenChest.lower()

            if OpenChest == "yes":
                PlayerGold += 5
                PlayerHealth += 5
                print("\nInside the chest there is 5 gold and a health potion, you drink it.(+5 health)")
        print("\nYou can go to the fountain room(Room 1), the chest room(Room 4), the reward room(Room 5), or the Boss room(Room 7)")
        Room6Direction = ""
        while Room6Direction not in ["room 1", "room 4", "room 5", "room 7"]:
            Room6Direction = input("\nWhere do you want to go?(Room 1, Room 4, Room 5, Room 7)\t")
            Room6Direction = Room6Direction.lower()

        if Room6Direction == "room 1":
            Room1()
        if Room6Direction == "room 4":
            Room4()
        if Room6Direction == "room 5":
            Room5()
        if Room6Direction == "room 7":
            Room7()

    def Room7():
        global PlayerGold
        print("\nYou push through the heavy doors and enter a big room. At the end of the room there the necromancer sits on his throne. You enter combat, good luck.")
        Combat(Boss)
        print(f"You won! You had {PlayerGold} gold.")
        quit()

    def IsPlayerDead():
        global PlayerHealth
        if PlayerHealth > 0:
            return
        elif PlayerHealth <= 0:
            print("\nYou have died. The End.")
            quit()

    def Combat(enemy):
        global PlayerSpeed, PlayerHealth, PlayerGold, Inventory, PlayerStrenght
        print(f"\nYou are now fighting the {enemy['Monster name']}.")

        if PlayerSpeed <= enemy["Speed"]:
            print(f"\nYou are slower than the {enemy['Monster name']}, so it will go first.")
            while True:
                print(f"\nThe {enemy['Monster name']} attacks and does {enemy['Attack']} damage.")

                PlayerHealth -= enemy["Attack"]
                IsPlayerDead()

                print(f"\nIt is your turn, you can attack or you can heal, your health is {PlayerHealth}.")
                CombatChoice = input("\nWhat do you want to do?(Attack, Heal)\t")
                CombatChoice = CombatChoice.lower()

                if CombatChoice == "heal":
                    if "Health Potion" in Inventory:
                        Inventory.remove("Health Potion")
                        PlayerHealth += 7

                        print(f"\nYou chose to heal, GLUG GLUG GLUG, now it is the monsters turn. Your health is now {PlayerHealth}.")
                    else:
                        print(f"\nYou do not have a health potion, your inventory is {Inventory}. You wasted your time.")
                        continue
                
                if CombatChoice == "attack":
                    if Inventory[0] == "Longsword":
                        enemy["Health"] -= (PlayerStrenght + 3)
                        print(f"\nYou attack the {enemy['Monster name']} BONK with your {Inventory[0]} and you do {PlayerStrenght + 3} damage. The monster has {enemy['Health']} left.")
                    elif Inventory[0] == "Shortsword":
                        enemy["Health"] -= (PlayerStrenght + 1)
                        print(f"\nYou attack the {enemy['Monster name']} SHANK with your {Inventory[0]} and you do {PlayerStrenght + 1} damage. The monster has {enemy['Health']} left.")

                    if enemy["Health"] <= 0:
                        print(f"\nYou beat the monster. You get {enemy['Reward']} gold.")
                        PlayerGold += enemy["Reward"]
                        return
                
                else:
                    print("\nYou think to hard. To bad.")
                            
        elif PlayerSpeed > enemy["Speed"]:
            while True:
                print(f"\nIt is your turn, you can attack or you can heal, your health is {PlayerHealth}.")
                CombatChoice = input("\nWhat do you want to do?(Attack, Heal)\t")
                CombatChoice = CombatChoice.lower()

                if CombatChoice == "heal":
                    if "Health Potion" in Inventory:
                        Inventory.remove("Health Potion")
                        PlayerHealth += 7

                        print(f"\nYou chose to heal, GLUG GLUG GLUG, now it is the monsters turn. Your health is now {PlayerHealth}.")
                    else:
                        print(f"\nYou do not have a health potion, your inventory is {Inventory}.")
                        continue
                
                if CombatChoice == "attack":
                    if Inventory[0] == "Longsword":
                        enemy["Health"] -= (PlayerStrenght + 3)
                        print(f"\nYou attack the {enemy['Monster name']} BONK with your {Inventory[0]} and you do {PlayerStrenght + 3} damage. The monster has {enemy['Health']} left.")
                        
                    elif Inventory[0] == "Shortsword":
                        enemy["Health"] -= (PlayerStrenght + 1)
                        print(f"\nYou attack the {enemy['Monster name']} SHANK with your {Inventory[0]} and you do {PlayerStrenght + 1} damage. The monster has {enemy['Health']} left.")

                    if enemy["Health"] <= 0:
                        print(f"\nYou beat the monster. You get {enemy['Reward']} gold.")
                        PlayerGold += enemy["Reward"]
                        return
                    
                else:
                    print("\nYou think to hard. To bad.")

                print(f"\nThe {enemy['Monster name']} attacks and does {enemy['Attack']} damage.")

                PlayerHealth -= enemy["Attack"]
                IsPlayerDead()

    def NarratorBoss():
        global PlayerGold, PlayerSpeed, PlayerStrenght, PlayerHealth, Inventory, Timeloop
        Timeloop += 1

        if Timeloop == 0:
            print("\nYou are entering combat.")
            time.sleep(0.25)
            print("\nLuck won't help you.")
            time.sleep(0.25)
            print("\nSet luck to 0, Gold to 0, Health to 10, Speed to 10, Stregnth to 1, Inventory to []")
            time.sleep(0.25)

            print("\nYou will now suffer for your sins against me. Set Health = 9")
            time.sleep(0.25)

            Finalaction1 = input("(Fight/Run)\t")

            print("\nYou can't do anything you are under my control.")
            time.sleep(0.25)
            print("\n Good bye little adventurer.")
            time.sleep(0.25)
            print("\nSet Health = 0")
            time.sleep(1)
            NarratorBoss()        

        elif Timeloop == 1:
            print("\nYou are entering combat.")
            time.sleep(0.5)
            print("\nLuck won't help you.")
            time.sleep(0.5)
            print("\nSet luck to 0, Gold to 0, Health to 10, Speed to 10, Stregnth to 1, Inventory to []")
            time.sleep(0.5)

            print("\nYou will now suffer for your sins against me. Set Health = 9")
            time.sleep(0.5)

            Finalaction2 = input("(Fight/Run)\t")

            print("\nYou can't do anything you are under my control.")
            time.sleep(0.5)
            print("\n Good bye little adventurer.")
            time.sleep(0.5)
            print("\nSet Health = 0")
            time.sleep(1.5)
            NarratorBoss()
        
        elif Timeloop == 3:
            Finalaction3 = input("(Fight/Run)")

            print("\nYou can't do anything you are under my control.")
            time.sleep(1)
            print("\n Good bye little adventurer.")
            time.sleep(1)
            print("\nSet Health = 0")
            time.sleep(2)
            NarratorBoss()
        
        elif Timeloop == 4:
            Finalaction4 = input("(Fight/Run)\t")
            Finalaction4 = Finalaction4.lower()

            if Finalaction4 in ["fight", "f"]:
                print("(Narrator Health -0)")
                time.sleep(1)
                print("\nYou can't do anything me.")
                time.sleep(1)
                print("\n Good bye little adventurer.")
                time.sleep(1)
                print("\nSet Health = 0")
                time.sleep(3)
                NarratorBoss()
            else:
                print("You can't run.")
                time.sleep(1)
                print("\n Good bye little adventurer.")
                time.sleep(1)
                print("\nSet Health = 0")
                time.sleep(3)
                NarratorBoss()
        
        elif Timeloop == 5:
            print("\nYou wake up in you bed, it was all a dream. You look around your room and you see the sunlight shining through the window. You feel refreshed and ready to start a new day.")



    print("\nAn evil necromancer is living in the old crypt down just out of town. The village has grown worried, so they have picked you to fight him. You have some basic items that they have given you. Good luck. Try to do it as fast as you can.")
    print("\nYou walk out of your house, down the cobblestone pathway, to the town center.")
    TownCenter()
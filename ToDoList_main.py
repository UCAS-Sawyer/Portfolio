#Sawyer Wood, To Do List

#This is error handling for integers
def intchecker(inputx):
    try:
        #Turning it into the int and returning it
        inputx = int(inputx)
        return inputx
    except:
        #If it can't be turned into a int then it will return them back to the UI 
        print("\nThat is an invalid input.")
        return None

#This reads the lines
def reading_lines():
    with open("ToDoList/To_Do_List.txt", "r") as file:
        lines = file.readlines()
        return lines

#It is counting how many lines are 
def number_of_lines():
    number_lines = 0
    with open("To_Do_List.txt", "r") as file:
        lines = file.readlines()
        number_lines = len(lines)
        return number_lines

#This adds the item and numbers it
def add_item(number_lines):
    with open("To_Do_List.txt", "a", newline= "") as file:
        item = input("\nWhat item would you like to add to your list?\n")
        file.write(f"{number_lines + 1}. {item}\n")
        print(f"\nItem |{item}| has been added to the list.")


#This checks off the line with "DONE!"
def check_off(number_lines):
    lines = reading_lines()
    item_position_to_check = intchecker(input("\nWhat item would you like to check off? (Give the number)\n"))

    #Checking to see if it is a valid input.
    if item_position_to_check is not None and 0 < item_position_to_check <= number_lines:
        print(f"\nItem {item_position_to_check} has been checked off.")
        item_position_to_check = item_position_to_check - 1#Getting the right position

        lines[item_position_to_check] = lines[item_position_to_check].strip() + " DONE!\n"  # Marking the line as done

        with open("To_Do_List.txt", "w") as file:
            file.writelines(lines)

    else:
        print("\nThat is an invalid input or item number out of range.")
    

#This removes a specified item from the to do lit
def remove_item(number_lines):
    lines = reading_lines()

    item_position_to_remove = intchecker(input("\nWhat item would you like to remove? (Give the number)\n"))

    if item_position_to_remove is not None and 0 < item_position_to_remove <= number_lines:
        lines.pop(item_position_to_remove - 1)  # Remove the specified line

        with open("To_Do_List.txt", "w", newline="") as file:
            for i, line in enumerate(lines, start=1):
                file.write(f"{i}. {line.split('. ', 1)[1]}")  # Renumber the items

        print(f"\nItem {item_position_to_remove} has been removed from the list.")
    else:
        print("\nThat is an invalid input or item number out of range.")

#Prints the list
def print_list():
    with open("To_Do_List.txt", "r") as file:
        for line in file:
            line_trimed = line.strip()
            print(f"\n{line_trimed}")
    return


#This is the main function
def main(number_lines):
    number_lines = number_of_lines()

    choice = input("\nWhat would you like to do, 1: Add An Item, 2: Check Off An Item, 3: Remove An Item, 4: See List, 5: Exit\n")

    if choice == "1":
        add_item(number_lines)
    elif choice == "2":
        print_list()
        check_off(number_lines)
    elif choice == "3":
        print_list()
        remove_item(number_lines)
    elif choice == "4":
        print_list()
    elif choice == "5":
        return
    else:
        print("\nThat is not an option.")
    
    main(number_lines)

#Clearing Screen
print("\033[H\033[J")
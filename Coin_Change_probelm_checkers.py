#Sawyer Wood Coin Changer problem, checkers

def float_checker(inputa, currency):
    try:
        inputa = float(inputa)
        if inputa <= 0:
            print("\nIt is not a valid number, try again")
            inputa = float_checker(input(f"\nHow much {currency} are you going to calculate?\n"), currency)
    except:
        print("\nThat is not a number.")
        inputa = float_checker(input(f"\nHow much {currency} are you going to calculate?\n"), currency)
    return inputa
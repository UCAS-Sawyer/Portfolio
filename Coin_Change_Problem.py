#Sawyer Wood Coin Changer problem

import csv

from Coin_Change_probelm_checkers import float_checker

def coin_change_main():

    def currency_type():
        currencies = "1. US Dollar, 2. Euro, 3. Pound, 4. Japanese Yen"

        currency = None

        while currency == None:
            currecny_type_choice = input(f"\nWhich available currecny are you inputing? {currencies}\n")

            if currecny_type_choice == "1":
                currency = "USD"
            elif currecny_type_choice == "2":
                currency = "Euro"
            elif currecny_type_choice == "3":
                currency = "Pound"
            elif currecny_type_choice == "4":
                currency = "Japanese-Yen"
            else:
                print("\nThat is not a valid input.")
                continue
            
            print(f"\nYou have selected the currecy {currency}.")
            return currency

    def reading_csv():
        #List of all the coins and bills
        coins_and_bills = []

        with open(f"Coin_Change_Problem_csvs\\{currency}.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                #Creating the dictionary

                coin_or_bill = {
                    "name" : row[0],
                    "amount" : int(row[1]),
                }
                coins_and_bills.append(coin_or_bill)

            return coins_and_bills

    currency = currency_type()
    coins_and_bills = reading_csv()
    
    amount = float_checker(input(f"\nHow much {currency} are you going to calculate?\n"), currency)

    if currency == "Japanese-Yen":
        amount = round(int(amount),0)
    else:
        amount = round(int(amount*100),2)

    
    solve(coins_and_bills, amount, currency)

def solve(coins_and_bills, amount, currency):

    x = 0
    money_used = []

    while amount > 0:
        amount -= coins_and_bills[x]["amount"]

        if amount < 0:
            amount += coins_and_bills[x]["amount"]
            x += 1
        elif amount == 0:
            money_used.append(coins_and_bills[x]["name"])
            break
        else:
            money_used.append(coins_and_bills[x]["name"])
    
    money_count = {}
    for money in money_used:
        if money in money_count:
            money_count[money] += 1
        else:
            money_count[money] = 1
    
    print("\nYou will need:")

    for money, count in money_count.items():
        print(f"{money}: {count}")
        

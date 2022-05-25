MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Total_amount":0
}
def report():
    print(f'Water : {resources["water"]}')
    print(f'Milk : {resources["milk"]}')
    print(f'Coffee : {resources["coffee"]}')
    print(f'Money : {resources["Total_amount"]}')
def reduce_resources(product):
    if product=="espresso":
        resources["water"]-=MENU[product]["ingredients"]["water"]
        resources["coffee"]-=MENU[product]["ingredients"]["coffee"]
    else:
        resources["water"]-= MENU[product]["ingredients"]["water"]
        resources["milk"] -= MENU[product]["ingredients"]["milk"]
        resources["coffee"] -= MENU[product]["ingredients"]["coffee"]
def product_details(product):
    reduce_resources(product)
    resources["Total_amount"]+=MENU[product]["cost"]
    return MENU[product]["cost"]
def main():
    print("Please insert coins..")
    coffee_cost = product_details(choice)
    print(f"The cost of {choice} is {coffee_cost}")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How many nickels? "))
    pennies = float(input("How many pennies? "))
    given_amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    given_amount = round(given_amount, 2)
    change_amount=given_amount-coffee_cost
    if given_amount >= coffee_cost:
        if given_amount>coffee_cost:
            print(f"Here is {given_amount} in change.")
        print(f"Here is your {choice} ☕️. Enjoy!")
    else:
        print(f"Sorry! Not enough money to buy this {choice}")
should_off=True
while should_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice== "off":
        should_off=False
        break
    if choice== "report":
        report()
    else:
        if resources["water"]<MENU[choice]["ingredients"]["water"]:
            print(f"Not enough water to make {choice}")
            should_insufficient=False
        elif resources["coffee"]<MENU[choice]["ingredients"]["coffee"]:
            print(f"Not enough coffee to make {choice}")
            should_insufficient = False
        else:
            if choice != "espresso":
                if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
                    print(f"Not enough milk to make {choice}")
                    should_insufficient = False
                else:
                    should_insufficient=True
            else:
                should_insufficient=True

        if should_insufficient:
            main()


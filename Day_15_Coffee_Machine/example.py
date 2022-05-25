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
}


def reduce_resources(product):
    resources["water"] = MENU[product]["ingredients"]["water"] - resources["water"]
    resources["milk"] = MENU[product]["ingredients"]["milk"] - resources["milk"]
    resources["coffee"] = MENU[product]["ingredients"]["coffee"] - resources["coffee"]
    return MENU[product]["cost"]
def espresso():
    resources["water"] = MENU[product]["ingredients"]["water"] - resources["water"]
    resources["coffee"] = MENU[product]["ingredients"]["coffee"] - resources["coffee"]
    return MENU[product]["cost"]
def latte():
    reduce_resources()
    return MENU[product]["cost"]
def cappuccino():
    reduce_resources(product)
    return MENU[product]["cost"]



product=input("What would you like?")
product()
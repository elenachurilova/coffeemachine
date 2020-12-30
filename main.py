# Print report -- resources left
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
    "money": 0,
}


while True:
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer == "report":
        for i in resources:
            if i == "money":
                print(f'{i.title()}: ${resources[i]}')
            elif i == "coffee":
                print(f'{i.title()}: {resources[i]} gr')
            else:
                print(f'{i.title()}: {resources[i]} ml')

    elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
        enough_ingredients = True
        for item in MENU[answer]["ingredients"]:
            if resources[item] >= MENU[answer]["ingredients"][item]:
                resources[item] -= MENU[answer]["ingredients"][item]
            else:
                enough_ingredients = False

        if enough_ingredients:
            print("Please insert coins.")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickles = input("how many nickles?: ")
            pennies = input("how many pennies?: ")

            print(f"Here's your {answer} ☕️ Enjoy!")
        else:
            print(f'Sorry there is not enough {item}')

    elif answer == "off":
        break
    else:
        print("I'm not sure I understand what you want 😕")
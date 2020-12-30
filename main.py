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
                print(f'Sorry there is not enough {item}')

        given_dollar_amount = 0
        if enough_ingredients:
            print("Please insert coins.")

            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            given_dollar_amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

            if given_dollar_amount >= MENU[answer]["cost"]:
                change = given_dollar_amount - MENU[answer]["cost"]
                resources["money"] += given_dollar_amount - change
                if change > 0:
                    print(f"Here is ${round(change, 2)} in change")
                print(f"Here's your {answer} ☕️ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif answer == "off":
        break
    else:
        print("I'm not sure I understand what you want 😕")
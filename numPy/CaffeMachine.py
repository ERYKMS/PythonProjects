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
money = 0


def check_request(request,menu, resources=resources, money=money):
    if request == "off":
        pass
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        return check_resources(request,menu)
    elif request == "report":
        for key in resources:
            if key == "coffee":
                print(f"{key}:{resources[key]}g")
            else:
                print(f"{key}:{resources[key]}ml")
        print(f"${money}")
        return resources

def check_resources(request, menu, resource=resources):
    for key in menu[request]["ingredients"]:
        if resource[key] >= menu[request]["ingredients"][key]:
            resource[key] -= menu[request]["ingredients"][key]
        else:
            print(f"Sorry, there is not enough {key}")
    return resource

coins={"quarters":0.25,"dimes":0.1,"nickles":0.05,"pennies":0.01}
def add_coins(coins=coins):
    result=0
    for key in coins:
        amount=int(input(f"How many{key}: "))
        result+=coins[key]*amount
    return result

def check_balance(request,money,menu=MENU):
    if money>=menu[request]["cost"]:
        money-=menu[request]["cost"]
        print(f"Here your {request} enjoy")
        return money
    else:
        print("Sorry that's not enough money. Money refunded.")
        return money


while True:
    request = input("What Would You Like (espresso/latte/cappuccino): ")
    if request == "off":
        break
    resources=check_request(request,MENU)
    if request!="report":
        money+=add_coins()
        money=check_balance(request,money)
        print(f"here is yoru {money} trade")


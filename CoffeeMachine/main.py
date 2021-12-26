import data

def getOrder():
    order = input('What would you like?(espresso/latte/cappuccino):')
    return order

def printResources():
    print(f'Water: {data.resources["water"]}ml')
    print(f'Milk: {data.resources["milk"]}ml')
    print(f'Coffee: {data.resources["coffee"]}g')
    print(f'Money:${data.resources["money"]}')

def checkResources(ingredients):
    """Checking Resources"""
    for item in ingredients:
        if ingredients[item] > data.resources[item]:
            print(f'Sorry there is not enough {item}.')
            return 0
    return 1

def getTotal(nbQ,nbD,nbN,nbP):
    return float(nbQ)*0.25+float(nbD)*0.1+float(nbN)*0.05+float(nbP)*0.01

def getCoins(drink):
    print("Please insert coins.")
    q = input("how many quarters?:")
    d = input("how many dimes?:")
    n = input("how many nickels?:")
    p = input("how many pennies?:")

    return getTotal(q,d,n,p)

def confirmOrder(order,total):
    water = data.MENU[order]["ingredients"]["water"]
    if(order != "espresso"):
        milk = data.MENU[order]["ingredients"]["milk"]
    coffee = data.MENU[order]["ingredients"]["coffee"]
    money = data.MENU[order]["cost"]

    data.resources["water"] -= water
    if (order != "espresso"):
        data.resources["milk"] -= milk
    data.resources["coffee"] -= coffee
    data.resources["money"] += money

    print(f'Here is ${round(total - data.MENU[order]["cost"],2)} in change.')
    print(f'Her is your {order}. Enjoy!')
    return


def startProcess(order):
    isAvail = checkResources(data.MENU[order]["ingredients"])

    if not isAvail:
        return
    total = getCoins(order)
    if data.MENU[order]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
    else:
        confirmOrder(order,total)
    return

order=""
while not order == "off":
    order = getOrder()
    if order == "report":
        printResources()
    elif order == list(data.MENU.keys())[0] or order == list(data.MENU.keys())[1] or order == list(data.MENU.keys())[2]:
        startProcess(order)
    elif order == "off":
        print("Bye")
    else:
        print('Wrong order!Please reselect')
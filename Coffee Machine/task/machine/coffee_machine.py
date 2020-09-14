machine_has = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'money': 550, 'disposable_cups': 9}

print(f"The coffee machine has:")
for ingredient, amount in machine_has.items():
    print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")

print()
action = input("Write action (buy, fill, take):")

# one cup contains the following
espresso = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'money': 4}
latte = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'money': 6}

drink = {1: espresso, 2: latte, 3: cappuccino}


def buy_coffee(item_to_buy):
    remainder = {}
    for k, v in item_to_buy.items():
        if k == 'money':
            remainder[k] = machine_has[k] + v
        else:
            remainder[k] = machine_has[k] - v
    remainder['disposable_cups'] = machine_has['disposable_cups'] - 1
    return remainder


def fill_coffee_machine(add_item):
    fill = {}
    for k, v in add_item.items():
        fill[k] = machine_has[k] + v
    fill['money'] = machine_has['money']
    return fill


# only for learning!!!
def take_money():
    global machine_has
    return machine_has['money']


if action == 'buy':
    what_buy = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    print()
    result = buy_coffee(drink[what_buy])
    print(f"The coffee machine has:")
    for ingredient, amount in result.items():
        print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")
elif action == 'fill':
    water_to_add = int(input("Write how many ml of water do you want to add:"))
    milk_to_add = int(input("Write how many ml of milk do you want to add:"))
    beans_to_add = int(input("Write how many grams of coffee beans do you want to add:"))
    cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:"))
    add_ingredient = {'water': water_to_add, 'milk': milk_to_add, 'coffee_beans': beans_to_add, 'disposable_cups': cups_to_add}
    machine_after_fill = fill_coffee_machine(add_ingredient)
    print()
    for ingredient, amount in machine_after_fill.items():
        print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")
elif action == 'take':
    print(f'I gave you ${take_money()}')
    machine_has['money'] = 0
    for ingredient, amount in machine_has.items():
        print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")

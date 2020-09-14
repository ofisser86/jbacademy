machine_has = {
    'water': 400,
    'milk': 540,
    'coffee_beans': 120,
    'money': 550,
    'disposable_cups': 9}


def print_remaining(machine):
    print(f"The coffee machine has:")
    for ingredient, amount in machine.items():
        print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")


def do_action():
    print()
    action_to_do = input("Write action (buy, fill, take, remaining, exit):")
    print()
    return action_to_do


action = do_action()

# one cup contains the following
espresso = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'money': 4}
latte = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'money': 6}

drink = {1: espresso, 2: latte, 3: cappuccino}


def buy_coffee(item_to_buy):
    if machine_has['water'] - item_to_buy['water'] < 1:
        return 'water'
    elif machine_has['milk'] != 'espresso' and machine_has['milk'] - item_to_buy['milk'] < 1:
        return 'milk'
    elif machine_has['coffee_beans'] - item_to_buy['coffee_beans'] < 1:
        return 'coffee_bean'

    machine_has['milk'] -= item_to_buy['milk']
    machine_has['water'] -= item_to_buy['water']
    machine_has['coffee_beans'] -= item_to_buy['coffee_beans']
    machine_has['disposable_cups'] -= 1
    machine_has['money'] += item_to_buy['money']


def fill_coffee_machine(add_item):
    for k, v in add_item.items():
        machine_has[k] = machine_has[k] + v
    machine_has['money'] = machine_has['money']


while action != 'exit':
    if action == 'buy':
        choose_option = input("What do you want to buy?"
                              " 1 - espresso,"
                              " 2 - latte,"
                              " 3 - cappuccino,"
                              " back - to main menu:")
        if choose_option == 'back':
            print()
            action = do_action()
            continue

        result = buy_coffee(drink[int(choose_option)])
        if result:
            print(f"Sorry, not enough {result}!")
            action = do_action()
        else:
            print('I have enough resources, making you a coffee!')
            action = do_action()
    elif action == 'fill':
        water_to_add = int(input("Write how many ml of water do you want to add:"))
        milk_to_add = int(input("Write how many ml of milk do you want to add:"))
        beans_to_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        add_ingredient = {'water': water_to_add, 'milk': milk_to_add, 'coffee_beans': beans_to_add,
                          'disposable_cups': cups_to_add}
        fill_coffee_machine(add_ingredient)
        action = do_action()
    elif action == 'take':
        print(f"I gave you ${machine_has['money']}")
        machine_has['money'] = 0
        action = do_action()
    elif action == 'remaining':
        print_remaining(machine_has)
        action = do_action()
    else:
        break

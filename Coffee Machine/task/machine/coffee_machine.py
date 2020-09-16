class CoffeeMachine:
    # one cup contains the following
    espresso = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'money': 4}
    latte = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'money': 7}
    cappuccino = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'money': 6}

    drink = {1: espresso, 2: latte, 3: cappuccino}

    # states of machine
    # 1 - choosing an action (initial state)
    # 2 - choosing a type of coffee
    state = 'choosing an action'

    def __init__(self):
        self.machine_has = {
            'water': 400,
            'milk': 540,
            'coffee_beans': 120,
            'disposable_cups': 9,
            'money': 550}

    def print_remaining(self):
        print(f"The coffee machine has:")
        for ingredient, amount in self.machine_has.items():
            print(f"{amount} of {ingredient if '_' not in ingredient else ingredient.replace('_', ' ')}")

    def fill_machine(self, adds):
        for k, v in adds.items():
            self.machine_has[k] = self.machine_has[k] + v

    def buy_coffee(self, item_to_buy):
        if self.machine_has['water'] - item_to_buy['water'] < 1:
            return 'water'
        elif self.machine_has['milk'] != 'espresso' and self.machine_has['milk'] - item_to_buy['milk'] < 1:
            return 'milk'
        elif self.machine_has['coffee_beans'] - item_to_buy['coffee_beans'] < 1:
            return 'coffee_bean'

        self.machine_has['milk'] -= item_to_buy['milk']
        self.machine_has['water'] -= item_to_buy['water']
        self.machine_has['coffee_beans'] -= item_to_buy['coffee_beans']
        self.machine_has['disposable_cups'] -= 1
        self.machine_has['money'] += item_to_buy['money']

    def user_input(self):
        if self.state == 'choosing an action':
            string = 'Write action (buy, fill, take, remaining, exit):'
        else:
            string = 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'
        return string


my = CoffeeMachine()
while True:
    action = input(my.user_input())
    print()
    if action == 'buy':
        my.state = 'choosing a type of coffee'
        choose_option = input(my.user_input())

        if choose_option == 'back':
            my.state = 'choosing an action'
            print()
            continue
        result = my.buy_coffee(my.drink[int(choose_option)])
        if result:
            print(f"Sorry, not enough {result}!")
        else:
            print('I have enough resources, making you a coffee!')
        my.state = 'choosing an action'
    elif action == 'remaining':
        my.print_remaining()
    elif action == 'fill':
        water_to_add = int(input("Write how many ml of water do you want to add:"))
        milk_to_add = int(input("Write how many ml of milk do you want to add:"))
        beans_to_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_to_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        add_ingredient = {'water': water_to_add, 'milk': milk_to_add, 'coffee_beans': beans_to_add,
                          'disposable_cups': cups_to_add}
        my.fill_machine(add_ingredient)
    elif action == 'take':
        print(f"I gave you ${my.machine_has['money']}")
        my.machine_has['money'] = 0
    elif action == 'exit':
        break

    print()

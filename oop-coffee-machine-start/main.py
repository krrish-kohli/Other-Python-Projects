from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    menu_items = menu.get_items()
    choice = input(f"What would you like? {menu_items}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)

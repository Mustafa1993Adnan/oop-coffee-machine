from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_machine_on = True
while is_machine_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? {options}: ")
    if choice == "reports":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_machine_on = False
    else:
        item = menu.find_drink(choice)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item):
                # money_received = money_machine.process_coins()
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)

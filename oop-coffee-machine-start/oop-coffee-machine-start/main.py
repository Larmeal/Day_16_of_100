from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
coffee_marker = CoffeeMaker()
money_machine = MoneyMachine()

again = True
while again:
    choice = order.get_items()
    order_menu = input(f"What would you like? ({choice}): ").lower()
    if order_menu == "report":
        coffee_marker.report()
        money_machine.report()
    elif order_menu == "off":
        print("Thank you, see you next times.")
        again = False
    else:
        order_coffee = order.find_drink(order_menu)
        if coffee_marker.is_resource_sufficient(order_coffee) and money_machine.make_payment(order_coffee.cost):
            coffee_marker.make_coffee(order_coffee)
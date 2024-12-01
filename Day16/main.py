from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
menu = Menu()
money  = MoneyMachine()

is_On= True

while is_On:
  choice = input(f"What would you like {menu.get_items()}")
  # print(choice)
  if choice=="report":
    coffeemaker.report()
    money.report()
  elif choice == "off":
    is_On=False
  else:
    drink = menu.find_drink(choice)
    if coffeemaker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
      coffeemaker.make_coffee(drink)
    
    
    
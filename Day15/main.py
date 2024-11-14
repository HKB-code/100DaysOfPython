MENU = {
  "expresso":{
    "ingredients":{
          "water":50,
           "coffee":18
  },
    "cost":1.5
  },
  "latte": {
    "ingredients":{
        "water":50,
         "coffee":18
  },
    "cost":2.5
  },
  "cacppuccino":{
    "ingredients":{
      "water": 250,
      "milk":100,
      "coffee":24
    },
    "cost":3.0
  }
}

resources = {
  "water": 300,
  "milk":200,
  "coffee":100
}

# TODO: 1. Print report of all coffee machine resources
def user_inputs():
  return input("What would you like? (expresso/latte/cacppuccino): ").lower()

should_continue = True
Money=0
def turn_Off():
  global should_continue
  should_continue = False

def isSufficient(userInputs,coin):
  if userInputs =="cacppuccino":
    if MENU[userInputs][ "ingredients"]["water"]> resources["water"]:
      print("Sorry there is no enough water")
    elif MENU[userInputs][ "ingredients"]["milk"]> resources["milk"]:
      print("Sorry there is no enough milk")
    elif MENU[userInputs][ "ingredients"]["coffee"]> resources["coffee"]:
      print("Sorry there is no enough coffee")
    elif MENU[userInputs]["cost"]>coin:
      print("Sorry that's not enough money. Money refunded.")
    return False
      
      
  elif userInputs=="espresso" or userInputs =="latte":
     if MENU[userInputs][ "ingredients"]["water"]> resources["water"]:
       print("Sorry there is no enough water")
     elif MENU[userInputs][ "ingredients"]["coffee"]> resources["coffee"]:
       print("Sorry there is no enough coffee")
     elif MENU[userInputs]["cost"]>coin:
       print("Sorry that's not enough money. Money refunded.")
     return False
  else:
    return True
    
    
def coins():
  quarters = int(input("How many quarters? "))
  dimes = int(input("How many dimes? "))
  nickles = int(input("How many nickle? "))
  pennies = int(input("How many pennies? "))
  coin = 0.25*quarters + 0.10 *dimes + 0.05*nickles+ 0.01*pennies
  return coin
    
    
def coins_refund(userInputs,money):
   ing = MENU[userInputs]
   if ing["cost"]<money:
    refund = round( money - ing["cost"],2)
    return refund
   
     
      
def make_drink(userInputs):
  items =  MENU[userInputs]["ingredients"]
  for item in items:
    resources[item] = resources[item] - items[item]
  return f"Here is your {userInputs}. Enjoy!"
    
    
  

while should_continue:
  userInputs =user_inputs()
  print(userInputs)
  
  if userInputs=='report':
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {Money}")
  elif userInputs=='off':
    turn_Off()
  else:
    amount = coins()
    success = isSufficient(userInputs,coin=amount)
    if success:
      refund_Money = coins_refund(userInputs=userInputs,money=amount)
      print(f"Here is ${refund_Money} dollars in change")
      Money+=MENU[userInputs]["cost"]
      drink = make_drink(userInputs=userInputs)
      print(drink)
    
    else:
      print("Sorry that's not enough money. Money refunded.")
      
      
      
     
     
     
    
    
     
    
   
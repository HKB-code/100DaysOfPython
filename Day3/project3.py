print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Treasure Island, Your mission is to find the treasure.")
road = input("You're at croos road. Where do you want to go? \n Type 'Left' or 'Right' ...\n")
if(road =="left" or road=="Left"):
  lake = input("You've come to a lake. There is an island in the middle of the lake. \n Type  'wait' to wait for a boat. Type 'swim' to swim across \n")
  if(lake=="wait"or lake=="Wait"):
    door = input("You arrived on the island 'unharmed'. There is a house with 3 doors. \n one red, one yellow, one blue. Which color do you choose? \n")
    if(door =="blue"or door=="Blue"):
      print("Eaten by beasts.Game Over.")
    elif(door =="yellow"or door=="Yellow"):
      print("You win the game")
    elif(door =="red"or door=="red"):
      print("It's the room full of fire. Game over") 
    else:
      print("You choose a door that dosen't exist. Game Over")
  else:
      print("Attacked by trout. Game Over.")
    
else:
 print("Fall into a hole.Game Over.")  
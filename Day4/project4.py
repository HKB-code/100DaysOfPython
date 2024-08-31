import random
user_input = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. \n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]

if user_input>=3:
  print("oops please select the right inputs...")
else:
  print(game[user_input])
  computer_input = random.randint(0,2)
  print(game[computer_input])
  if(computer_input==0 and user_input==2):
    print("You lose")
  elif(computer_input==2 and user_input==0):
    print("You win")
  elif(computer_input>user_input):
    print("you lose")
  elif(computer_input<user_input):
    print("you win")
  else:
    print("Draw")
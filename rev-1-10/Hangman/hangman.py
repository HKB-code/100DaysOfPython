import random
word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]
stages = [ r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
                   
                               
##First Version                                
# print("Welcome to the Hangman...")
# print(logo)                                                              
# choosen_word = random.choice(word_list)
# wordLen = len(choosen_word)
# display = ["_"]*wordLen
# should_continue=True
# lives = 6
# print(display)
# print("You have 6 lives...")
# while should_continue:
  
#   guess = input("Guess the letter.. ").lower()
#   if guess in display:
#     print("You've already guess the letter....")
#     continue
#   for index in range(wordLen):
#     letter = choosen_word[index]
#     if letter==guess:
#       display[index] = letter
#       print(display)
      
#   if guess not in choosen_word:
#     lives-=1
#     print("You lost a live" if lives==5 else ("You lost another lives"))
#     print(f"{lives} lives left ")
      
#     if lives==0:
#       print("You lost the game..")
#       should_continue=False;

#   if "_" not in display:
#     print("you win")
#     should_continue=False
#   print(stages[lives])


# # Second Version
# your_previous_record={}
# play_count=0
# def updateLeadboard(attempts,lives):
#   attempt = f"{attempts} game"
#   leadBoard= {
#     attempt : lives
#   }
#   your_previous_record.update(leadBoard)
  
# def hangman():
#  global play_count
#  play_count+=1
#  print(logo)
#  choosen_word = random.choice(word_list)
#  print(choosen_word)
#  word_len = len(choosen_word)
#  display = ["_"]*word_len
#  print(display)
#  lives=6
#  end_of_game= False
#  while not end_of_game:
  
#   guess= input("Guess the letter...")
#   if guess in display:
#     print("You already guess the letter...")
#     continue;
#   for index in range(word_len):
#     letter= choosen_word[index]
#     if letter==guess:
#       display[index] = letter;
#       print(display)
#   if guess not in choosen_word:
#       lives-=1
#       if lives==0:
#         print("You lost the game")
#         end_of_game=True
#         print(stages[lives])
        
#         save_Records = input("Do you want to Save Your recods...Type 'y' or 'n'....." ).lower()
#         if save_Records=='y':
          
#           updateLeadboard(attempts=play_count, lives=lives)
        
#         print(your_previous_record)
        
#         want_to_play_again = input("Want to play again, Type 'Y' or Tye 'n'....").lower()
#         if want_to_play_again=='y':
#            hangman()
#         # elif want_to_play_again=='n'
          
        
#   print(stages[lives])
  
#   if "_" not in display:
#     print("You win")
#     end_of_game =True  
#     save_Records = input("Do you want to Save Your recods...Type 'y' or 'n'....." ).lower()
#     if save_Records=='y':
     
#      updateLeadboard(attempts=play_count, lives=lives)
#     print(your_previous_record)
    
#     want_to_play_again = input("Want to play again, Type 'Y' or Tye 'n'....").lower()
#     if want_to_play_again=='y':
#       hangman()

# hangman() 
# play_again = input("Want to play again, Type 'Y' or Tye 'n'....")
# while play_again =='Y':
#   hangman()
  
  
    #   # Version:3
    # #I want to save the user data:For this you need a a file that can store the information, so we use JSON
import json
your_previous_record={}
play_count=0
def save_data():
  with open('user_data.json','w') as file:
    json.dump(your_previous_record,file)
    
    
def load_data():
  global your_previous_record
  try:
    with open('user_data.json','r') as file:
      your_previous_record = json.load(file)
  except FileNotFoundError:
    your_previous_record={}
    
    
def display_data():
    load_data()
    print("User Data:", your_previous_record)

    
def manage_data():
    manage_choice = input("Do you want to delete the game data or save it? Type 'delete' or 'save': ").lower()
    if manage_choice == 'delete':
        your_previous_record.clear()
        save_data()
        print("Game data deleted.")
    elif manage_choice == 'save':
        save_data()
        print("Game data saved.")
    else:
        print("Invalid choice. Data will be saved by default.")
        save_data()
        print("Game data saved.")   
    
    
def updateLeadboard(attempts,lives):
  attempt = f"{attempts} game"
  leadBoard= {
    attempt : lives
  }
  your_previous_record.update(leadBoard)
  
def hangman():
 global play_count
 play_count+=1
 print(logo)
 choosen_word = random.choice(word_list)
 print(choosen_word)
 word_len = len(choosen_word)
 display = ["_"]*word_len
 print(display)
 lives=6
 end_of_game= False
 while not end_of_game:
  
  guess= input("Guess the letter...")
  if guess in display:
    print("You already guess the letter...")
    continue;
  for index in range(word_len):
    letter= choosen_word[index]
    if letter==guess:
      display[index] = letter;
      print(display)
  if guess not in choosen_word:
      lives-=1
      if lives==0:
        print("You lost the game")
        end_of_game=True
        print(stages[lives])
        
        save_Records = input("Do you want to Save Your recods...Type 'y' or 'n'....." ).lower()
        if save_Records=='y':
          
          updateLeadboard(attempts=play_count, lives=lives)
        
        print(your_previous_record)
        
        want_to_play_again = input("Want to play again, Type 'Y' or Tye 'n'....").lower()
        if want_to_play_again=='y':
           hangman()
        
          
        
  print(stages[lives])
  
  if "_" not in display:
    print("You win")
    end_of_game =True  
    save_Records = input("Do you want to Save Your recods...Type 'y' or 'n'....." ).lower()
    if save_Records=='y':
     
     updateLeadboard(attempts=play_count, lives=lives)
    print(your_previous_record)
    
    want_to_play_again = input("Want to play again, Type 'Y' or Tye 'n'....").lower()
    if want_to_play_again=='y':
      hangman()
      display_data()

    else:
      manage_data()
      
      
      
      
display_data()

hangman() 


# Version 4
#  #So you want to save data of each user so that if they want to see their data , so for this you need to asign an unique Id and manage their data accordingly and you need a JSON file so that it can store your data or current state..




import random,hangman_words
from Hangman import logo, stages
print('Welcome To The Hangman')
print(logo)
print("You Have 6 lives...")
choosenWord = random.choice(hangman_words.word_list)
wordLen  = len(choosenWord)
display= ["_"]*wordLen



endOfGame = False
lives =6
while not endOfGame:
  guess = input("Guess the letter: ").lower()
  if guess in display:
    print("You already Guess the letter...")
    continue
  for index in range(wordLen):
    letter = choosenWord[index]
    if guess == letter:
      display[index]=letter
  if guess not in choosenWord:
    lives-=1
    if lives>0:
      print("Oops you lose 1 live..." if lives==5 else "You lose another live.." )
      print(f"{lives} lives left")
      
    elif lives==0:
      endOfGame =True
      print("You Lose")
      print(f"The word is {choosenWord}")
      
  print("".join(display))
  
  if "_" not in display:
    endOfGame = True
    print("You Win")
    
  print(stages[lives])
  
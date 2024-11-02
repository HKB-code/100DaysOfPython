
  





# def ceaser(original_Text,shift_Amount, encode_or_decode):
#  alpha_list1 = [ chr(i) for i in range(ord('a') , ord("z")+1)]
#  alpha_list2 = [ chr(i) for i in range(ord('A') , ord("Z")+1)]

#  shift_Text = ""
#  if encode_or_decode =="decode":
#    shift_Amount*=-1
#  for letter in original_Text:
#    if letter in alpha_list1:
#      ind = alpha_list1.index(letter)
#      shift_position = ind+shift_Amount
#      shift_position%=len(alpha_list1)
#      shift_Text += alpha_list1[shift_position]
#    elif letter  in alpha_list2:
#      ind = alpha_list2.index(letter)
#      shift_position = ind+shift_Amount
#      shift_position%=len(alpha_list2)
     
#      shift_Text += alpha_list2[shift_position]
#    else:
#      shift_Text+=letter
 
#  print(shift_Text)



# should_continue=True
# while should_continue:
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#   if direction =="encode" or direction=="decode":
#    text = input("Type your Message...\n")
#    shift = int(input("Type the shift number:\n"))
#    ceaser(text,shift,direction)
#    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
#    if restart =='no':
#     should_continue=False
#     print("Bye..")
#   else:
#     print("Try Again")
  
    
def ceaser(original_text,shift,encode_or_decode):
  alpha_list1 = [chr(i) for i in range(ord('a'), ord('z')+1)]
  alpha_list2 = [chr(i) for i in range(ord('A'), ord('Z')+1)]
  numbers = list(range(0,10))
  number_list = [str(num) for num in numbers]
  print(number_list)
  reverse_letter=[]
  
  
  
  shift_text=""
  if encode_or_decode == 'decode':
    shift*=-1
  for letter in original_text:
    if letter in alpha_list1:
      ind = alpha_list1.index(letter)
      shift_position = ind+shift
      shift_position%=len(alpha_list1)
      shift_text += alpha_list1[shift_position]
    elif letter in alpha_list2:
      ind = alpha_list2.index(letter)
      shift_position = ind+shift
      shift_position%=len(alpha_list1)
      shift_text += alpha_list1[shift_position]
    elif letter in number_list:
      ind = number_list.index(letter)
      shift_position = ind+shift
      shift_position%=len(number_list)
      shift_text += number_list[shift_position]
    elif letter==" ":
     shift_text+=letter
    else:
      reverse_letter += letter.split(",")
  if encode_or_decode=="encode":
   shift_text+=("").join(reverse_letter[::-1])
  else:
   shift_text+=("").join(reverse_letter[::-1])
    
        
        
  print(shift_text)
      
      


should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction =='encode' or "decode":
    text = input("Write Your message: ").lower()
    shift_amount = int(input("Type the shift number: "))
    ceaser(original_text=text,shift=shift_amount,encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if restart =='no':
     should_continue=False
     print("Bye..")
    else:
     print("Try Again")
    
    
    
    

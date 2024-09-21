
  





def ceaser(original_Text,shift_Amount, encode_or_decode):
 alpha_list1 = [ chr(i) for i in range(ord('a') , ord("z")+1)]
 alpha_list2 = [ chr(i) for i in range(ord('A') , ord("Z")+1)]

 shift_Text = ""
 if encode_or_decode =="decode":
   shift_Amount*=-1
 for letter in original_Text:
   if letter in alpha_list1:
     ind = alpha_list1.index(letter)
     shift_position = ind+shift_Amount
     shift_position%=len(alpha_list1)
     shift_Text += alpha_list1[shift_position]
   elif letter  in alpha_list2:
     ind = alpha_list2.index(letter)
     shift_position = ind+shift_Amount
     shift_position%=len(alpha_list2)
     
     shift_Text += alpha_list2[shift_position]
   else:
     shift_Text+=letter
 
 print(shift_Text)



should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction =="encode" or direction=="decode":
   text = input("Type your Message...\n")
   shift = int(input("Type the shift number:\n"))
   ceaser(text,shift,direction)
   restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
   if restart =='no':
    should_continue=False
    print("Bye..")
  else:
    print("Try Again")
  
    

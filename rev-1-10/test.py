def upperWORD(str):
  estr = str.split()
  upstr=""
  # Method-1
  
  # for i in range(len(estr)):
  #   upstr += estr[i][0].upper() + estr[i][1:] + " "
    
  # print(upstr)
  for word in estr:
    upstr +=word[0].upper()+ word[1:]+" "
  print(upstr)
    
    
upperWORD("harshil jain")
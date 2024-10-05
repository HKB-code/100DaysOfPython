def is_leap_year():
   try:
     year = int(input("Enter the Year..."))
   except ValueError:
     print("Print a valid year....")
     return
    
   if year%4==0:
     if year%100==0:
       if year%400==0:
         print("Leap Year")
       else:
         print("Not a Leap Year")
     else:
        print("Leap Year")
   else:
     print("Not a Leap Year")
     
is_leap_year()


 # # Clean Code
def is_leap_year_cleanCode():
   try:
     year = int(input("Enter the Year..."))
   except ValueError:
     print("Print a valid year....")
     return
    
   if (year%4==0 and (year%100!=0 or year%400==0)):
     print(f"{year} is a Leap Year...")
   else:
     print(f"{year} is not a Leap Year...")
     
is_leap_year_cleanCode()
from art import logo
print("Welcome TO The Secret Blind Auction")
print(logo)
final_bid = {}
should_continue=True
def add_Bid():
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))
  bid_data = {
      name:bid
     }
  final_bid.update(bid_data)


while should_continue:
  add_Bid()
  extra= input("Are there any other bidders? Type 'yes or 'no'.\n").lower() 
  if( extra=='no'):
     bidder_name=""
     max_bid = 0
     for key in final_bid:
       bid_amount = final_bid[key]
       if bid_amount>max_bid:
         max_bid=bid_amount
         bidder_name = key
         
     print(f"The winner is {bidder_name} with a bid of ${max_bid}")
    
     should_continue=False
 
    
    

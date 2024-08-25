# from replit import clear

print("welcome to the secret auction program")

print("enter bidder name")


bidder = {}
continue_bid = True

# to clear the console after each bid 
clear = lambda: print("\033c", end="", flush=True)

highest_bid = 0
winner = ""


while continue_bid:
  name= input("enter your name: ")
  bid = int(input("enter your bid: $"))

  bidder[name] = bid

  # check for other bidders 
  other_bidders = input("are there any other bidders? type 'yes' or 'no'\n: ")
  if other_bidders == "yes":
    clear()
  else:
    continue_bid = False
 # find the highest bid 


for bid in bidder:
  # print(bidder)
  #print(f"bidder name is {bid}") # this will print the name of the bidder which key
  #print(f"bidder bid is {bidder[bid]}") # this will print the bid of the bidder
  if bidder[bid] > highest_bid:
    highest_bid = bidder[bid]
  
    winner = bid

print(f"the winner is {winner} with a bid of ${highest_bid}")

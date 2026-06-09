# import os
# data={}
# def find_winner(bidder_details):
#     highest_bid=0
#     winner=""
#     for bidder in bidder_details:
#         bid_price=bidder_details[bidder]
#         if bid_price>highest_bid:
#             highest_bid=bid_price
#             winner=bidder
#     print(f"The winner is {winner} with a bid price of {highest_bid}")
# print("********** Welcome to silent auction **********")
# stop=True
# while stop:
#     name = input("Enter your name: ")
#     price = int(input("Enter your bid price: "))
#     data[name]=price
#     to_stop=input("Do you want to stop silent auction? (y/n): ").lower()
#     if to_stop=="n":
#         stop=False
#         find_winner(data)
#     elif to_stop=="y":
#         os.system("cls")



































import os
data={}
def highest_price(details):
    highest_bid=0
    winner=""
    for bidder in details:
        bid=details[bidder]
        if bid>highest_bid:
            highest_bid=bid
            winner=bidder
    print(f"Winner is {winner} with price {highest_bid}")
print("WELCOME TO SILENT AUCTION")
to_continue=True
while to_continue:
    name=input("Enter your name: ")
    price=int(input("Enter your price: "))
    data[name]=price
    stop=input("Do you want to continue: (y/n): ")
    if stop=="y" or stop=="Y":
        os.system("cls")
    else:
        to_continue=False
        highest_price(data)






























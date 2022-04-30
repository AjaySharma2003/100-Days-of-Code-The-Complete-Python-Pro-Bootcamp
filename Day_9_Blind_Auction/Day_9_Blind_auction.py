from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welocome to the secret auction program.")
bidding_details=[]
choice="yes"
while(choice!="no"):
    add_dict={}
    add_dict["name"]=input("What is your name?: ")
    add_dict["bid"]=int(input("What is your bid?: $"))
    bidding_details.append(add_dict)
    choice=input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    clear()
maximum_bid=0
name=""
for i in range(0,len(bidding_details)):
    if maximum_bid<bidding_details[i]["bid"]:
        maximum_bid=bidding_details[i]["bid"]
        name=bidding_details[i]["name"]
print(f"The winner is {name} with a bid of ${maximum_bid}")
import random
from replit import clear
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def random_card_generator():
    card_choice=random.choice(cards)
    return card_choice
choice="y"
computer_choice="y"
def user_input(choice):
        user_cards=[]
        user_cards.append(random_card_generator())
        while(choice!="n"):
            user_cards=check_ace(user_cards)
            user_cards.append(random_card_generator())
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print("Computer's first card : ",computer_cards[0])
            if sum(user_cards)>=21:
                choice="n"
            else:
                choice=input("Type 'y' to get another card, type 'n' to pass : ")
            if sum(user_cards)<17 and choice=="n":
                choice=input("You should not pause at these moment.Please type 'y'")
        return user_cards
def computer_input(computer_choice):
    computer_cards=[]
    computer_cards.append(random_card_generator())
    while(computer_choice!="n"):
        computer_cards=check_ace(computer_cards)
        computer_cards.append(random_card_generator())
        if sum(computer_cards)>=17 and sum(computer_cards)<21:
            computer_choice="n"
        if sum(computer_cards)>=21:
            computer_choice="n"
        if sum(computer_cards)<17:
            computer_choice="y"
    return computer_cards
def check_ace(cards):
    for i in range(2):
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return cards
def result():
    user_final_cards=check_ace(user_cards)
    computer_final_cards=check_ace(computer_cards)
    user_final_score=sum(user_final_cards)
    computer_final_score=sum(computer_final_cards)
    print(f"Your final hand: {user_final_cards}, final score: {user_final_score}")
    print(f"Computer's final hand: {computer_final_cards}, final score: {computer_final_score}")
    if user_final_score>21 or computer_final_score>21:
        if user_final_score>21:
            print("You lose")
        elif computer_final_score>21:
            print("You Win")
    elif user_final_score==computer_final_score:
        print("Draw")
    else:
        if user_final_score>computer_final_score:
            print("You Win")
        else:
            print("You lose")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")!="n":
    clear()
    print(logo)
    user_cards = []
    computer_cards = []
    computer_cards=computer_input(computer_choice)
    user_cards=user_input(choice)
    result()

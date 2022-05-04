from game_data import data
import random
import art
# from replit import clear
A=random.choice(data)
B=random.choice(data)
should_end=True
choice=""
answer=False
score=0
print(art.logo)
while should_end:
    print(f'Compare A : {A["name"]}, a {A["description"]}, from {A["country"]}')
    print(art.vs)
    print(f'Against B : {B["name"]}, a {B["description"]}, from {B["country"]}')
    choice=input("Who has more followers? type 'A' or 'B' : ")
    if A["follower_count"]>B["follower_count"]:
        answer="A"
    else:
        answer="B"
    if choice==answer:
       #
       print(art.logo)
       score+=1
       print(f"You're correct! current score : {score}")
       A=B
       B=random.choice(data)
    else:
       # clear()
       print(f"Sorry, that's wrong. Final Score : {score}")
       should_end=False
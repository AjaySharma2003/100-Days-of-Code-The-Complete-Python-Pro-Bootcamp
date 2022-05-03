import random
from art import logo
print(logo)
answer=random.randint(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard' : ")
if difficulty=="easy":
    attempts=10
else:
    attempts=5
should_continue=True
while should_continue:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_input=int(input("Make a guess : "))
    if user_input>answer:
        print("Too High.")
    else:
        print("Too Low.")
    if attempts==1 or user_input==answer:
        should_continue=False
    else:
        print("Guess again.")
    attempts-=1
if user_input==answer:
    print(f"You got it! The answer is {answer}")
else:
    print("You've run out of guesses, You Lose")
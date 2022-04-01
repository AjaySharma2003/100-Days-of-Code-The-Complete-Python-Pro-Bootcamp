import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissors=[rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for Rock,1 for paper or 2 for scissors."))
print("User input")
print(rock_paper_scissors[user_input])
computer_choice=random.randint(0,2)
print("Computer choice")
print(rock_paper_scissors[computer_choice])
win='''
              You Win!
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
               '''
lose="You Lose"
result=" "
if user_input==0 and computer_choice==2:
    result=win
elif user_input==0 and computer_choice==1:
    result=lose
if user_input==1 and computer_choice==0:
    result=win
elif user_input==1 and computer_choice==2:
    result=lose
if user_input==2 and computer_choice==1:
    result=win
elif user_input==2 and computer_choice==0:
    result=lose
if user_input==computer_choice:
    result="Draw!"
print(result)

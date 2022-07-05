print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right"')
if direction.lower()=="left":
    choice=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Typr "swim" to swim across.')
    if choice.lower()=="wait":
        door=input('You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour do you choose?')
        if door.lower()=="red":
            print("Burned by fire.\n Game Over")
        elif door.lower()=="blue":
            print("Eaten by beasts.\n Game Over")
        elif door.lower()=="yellow":
            print("You Win!")
        else:
            print("Please use the correct Key")

    else:
        print("Attacked by trout. Game Over")
else:
    print("Fall into a hole.\nGame Over.")

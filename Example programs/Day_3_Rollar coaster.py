height=int(input("Enter the Height : "))
if height<120:
    print("Sorry!! You are not allowed to Ride in Rollar Coaster")
else:
    print("Welcome")
    age=int(input("Enter the age : "))
    if age<12:
        cost=3
        print(f"You Should Pay {cost}$")
    elif age<19:
        cost=5
        print(f"You Should Pay {cost}$")
    elif age<26:
        cost=7
        print(f"You Should Pay {cost}$")
    elif age>=45 and age<=55:
        cost=0
        print("Have a  free ride on us!")
    else:
        cost=10
        print(f"You Should Pay {cost}$")
    wants_photo=int(input("If you want Photo enter 1 and you don't want enter 2 : "))
    if wants_photo==1:
        cost=cost+3
        print(f"You should pay {cost}$ for ride with photo")
    else:
        print(f"You should pay {cost}$ for ride")
    

print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip_percentage=float(input("What percentage tip would you like to give? 10,12, or 15? "))
no_of_people=int(input("How many people to split the bill? "))
tip=bill*tip_percentage/100
total_bill=bill+tip
each_people=round(total_bill/no_of_people,2)
print(f"Each person should pay: {each_people}")

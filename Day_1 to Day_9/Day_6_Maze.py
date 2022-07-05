def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
while at_goal()!="true":
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()
    else:
        turn_left()
    
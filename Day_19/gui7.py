from turtle import Turtle, Screen
import random

is_on = False
sc = Screen()
sc.setup(width=500,height=400)

user_bet= sc.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter the color of its shell: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pxns = [-70, -40, -10, 20,50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_pxns[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True
    
while is_on:
    for turtle in all_turtles:
        
        if turtle.xcor() > 230:
            is_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("You've won the race !")
            else:
                print("U lost bro !")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

sc.exitonclick()
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time



t = Turtle()
sc = Screen()
sc.setup(600,600)  
sc.bgcolor("black")
sc.tracer(0)
sc.title("Sssssnake Game 🐍")

snake = Snake()
food = Food()
scr = Scoreboard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.09)
    snake.move()
    
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scr.in_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scr.reset()
        snake.reset()
        
    
    for segment  in snake.segment[1:]:
        if  snake.head.distance(segment) < 10:
            scr.reset()








sc.exitonclick()
from turtle import Turtle , Screen

sc = Screen()
tm = Turtle()

def fow():
    tm.shape("turtle")
    tm.color("yellow")
    tm.forward(50)
    
    
sc.listen()
sc.onkey(key ="space", fun= fow)    
sc.exitonclick()
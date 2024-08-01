import turtle as t
import random

tt =  t.Turtle()
t.pensize(5)

t.shape('turtle')



def forw():
    t.forward(100)
  
def fow():
    t.backward(100)
    
def clock():
    t.right(10) 
    
def anti():
    t.left(10)  
    
def c():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    

sr = t.Screen()
t.listen()
t.onkey(forw, "W")
t.onkey(fow, "S")
t.onkey(clock, "A")
t.onkey(anti, "D")

t.exitonclick()
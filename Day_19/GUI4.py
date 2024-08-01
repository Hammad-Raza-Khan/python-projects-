import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
    
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.pensize(10)
t.shape('turtle')
t.speed("fastest")

def making_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g , b)
    return color
    


for n in range(200):
    t.color(making_colours())
    t.forward(50)
    t.setheading(random.choice(directions))
 
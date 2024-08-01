from turtle import *
import random
t = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def shapes(sides):
    angle  = 360/sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)
    
for _ in range(3, 10):
    t.color(random.choice(colours))
    shapes(_)

from turtle import Turtle, Screen


STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self) :
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        new1 = Turtle("square")
        new1.color("white")
        new1.penup()
        new1.goto(position)
        self.segment.append(new1)
            
            
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
        
    
    def extend(self):
        self.add_segment(self.segment[-1].position())
        
            
    def move(self):
        for s_num in range(len(self.segment) - 1, 0 , -1):
            x_follow_up = self.segment[s_num -1].xcor()
            y_follow_up = self.segment[s_num -1].ycor()
            self.segment[s_num].goto(x_follow_up, y_follow_up)
        self.head.forward(20)
        
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
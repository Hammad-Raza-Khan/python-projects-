from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font =("Arabic", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()
       
       
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align="center", font =("Arabic", 24, "normal"))
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
    
    
    # def gameover(self):
    #     self.goto(0,0)
    #     self.write(" GAME OVER ! ", align="center", font =("Arabic", 24, "normal"))
        
    def in_score(self):
        self.score += 1
        self.update_scoreboard()
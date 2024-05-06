from turtle import Turtle

FONT = ('Courier',20)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_score()

    def gameOver(self):
        self.goto(0,0)
        self.write(f'Game Over ☠️',align='center',font=FONT)

    def update_level(self):
        self.level += 1
        self.update_score()
    def update_score(self):
        self.goto(-280,250)
        self.clear()
        self.write(f'Level : {self.level}',align='left',font=FONT)




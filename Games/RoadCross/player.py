from turtle import Turtle
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.move()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def successful_crossing(self):
        if self.ycor() >= FINISH_LINE:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)


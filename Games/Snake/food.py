import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.create_food()

    def create_food(self):
        food_x = random.randint(-280, 208)
        food_y = random.randint(-280, 208)
        self.goto(food_x, food_y)


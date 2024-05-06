import random
import turtle
from turtle import Turtle

STARTING_POSITIONS = [[(0, 0), (-20, 0), (-40, 0)],
                      [(0, 20), (0, 40), (0, 60)],
                      [(20, 0), (40, 0), (60, 0)],
                      [(0, -20), (0, -40), (0, -60)]
                      ]
MOVE_DISTANCE = 20


class Snake:
    """ Everything Related to Snake is here"""
    # TODO 1 : Edit Add different starting positions. sol: list of list of tuples. 1 added.
    # E-W, N-S, W-E, S-N

    starting_position = random.choice(STARTING_POSITIONS)

    def __init__(self):
        self.game_level = " "
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        self.snake_head.color("grey")
        self.snake_length = len(self.snake_segments)

    def create_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def snake_reset(self):
        for dead_seg in self.snake_segments:
            # dead_seg.goto(1000,1000) # Out of Screen
            dead_seg.color('black') # Bg Colour
        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]
        self.snake_head.color("grey")
        self.snake_length = len(self.snake_segments)


    def grow(self):
        self.add_segment(self.snake_segments[-1].position())  # Getting hold of pos of last segment and adding segment

    def add_segment(self, position):
        segment = Turtle(shape="square")  # Bug that turtle segment head drn != head's head drn-> fixed!
        segment.penup()
        segment.color("white")
        segment.goto(position)
        if position in STARTING_POSITIONS[0]:
            segment.setheading(0)
        elif position in STARTING_POSITIONS[1]:
            segment.setheading(270)
        elif position in STARTING_POSITIONS[2]:
            segment.setheading(180)
        elif position in STARTING_POSITIONS[3]:
            segment.setheading(90)
        self.snake_segments.append(segment)

    def screen_continue(self):
        if self.game_level == "easy":
            # print(self.game_level)  # Later to be displayed in console -> debug
            current_x = self.snake_head.xcor()
            current_y = self.snake_head.ycor()
            if self.snake_head.xcor() > 280 or self.snake_head.xcor() < -280:
                print(f"snake.screen_continue xcor: {self.snake_head.xcor()}")
                self.snake_head.goto(current_x * -1, current_y)
            elif self.snake_head.ycor() > 280 or self.snake_head.ycor() < -280:
                print(f"snake.screen_continue ycor: {self.snake_head.ycor()}")
                self.snake_head.goto(current_x, current_y * -1)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            # Getting hold of previous segment
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            # Assigning values to next segment
            self.snake_segments[seg_num].goto(new_x, new_y)
            # TODO :  Setting direction of segments as one prior. Bug Fix
            head_is = self.snake_segments[seg_num - 1].heading()
            self.snake_segments[seg_num].setheading(head_is)
        # Moving first segment
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

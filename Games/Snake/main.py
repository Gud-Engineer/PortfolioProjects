"""
Classic Snakes Game.
1. Moving snake body 2. Eats food and grows in length 3. Difficulty increase :Don't get tangled
"""
import random
from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake


# TODO 1 : Create a snake body - done
# TODO 2 : Move the snake - Done
# TODO 3 : Control the snake - Done
# TODO 4 : Detect collision with food
# TODO 5 : Create Scoreboard
# TODO 6 : Detect collision with wall
# TODO 7 : Detect collision with tail
def set_game_level():
    """ Sets game level. one turtle is 20x20. 5 Segments=100 pixels."""
    if len(snake.snake_segments) < 5:
        return "easy"
    elif 5 <= len(snake.snake_segments) < 15:
        return "medium"
    else:
        return "hard"


def game_over():
    global game_is_on
    game_is_on = False
    print('Pressed q -> Exiting !!\nHave a Nice Day 😊')



# TODO Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)

# TODO creating snake
snake = Snake()
# print(snake.snake_head.heading())

# TODO Creating food
food = Food()

# TODO Create scoreboard
score = Scoreboard()
# score.score_level= set_game_level()
# TODO move snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.update()

game_is_on = True
screen.onkey(game_over, "q")
while game_is_on:
    level = set_game_level()
    snake.game_level = level
    score.score_level = level
    score.clear()
    score.update_scoreboard()
    if level != "medium":
        screen.update()
        time.sleep(0.5)
    else:
        screen.update()
        time.sleep(0.1)
    snake.screen_continue()  # To impose game over by wall crash.
    snake.move()
    # print(f"level {level} in main")
    # Collision with food
    if snake.snake_head.distance(food) < 15:
        food.create_food()
        score.increase_score()
        snake.grow()

    # TODO Detect Collision with wall
    if level != "easy":
        if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
            # game_is_on = False
            # score.gameOver()
            score.dead_snake()
            time.sleep(1)
            score.reset_game()
            snake.snake_reset()
        # TODO Collision with tail
        for segment in snake.snake_segments[1:]:
            if snake.snake_head.distance(segment) < 10:
                # game_is_on = False
                # score.gameOver()
                score.dead_snake()
                time.sleep(19)
                score.reset_game()
                snake.snake_reset()

screen.exitonclick()








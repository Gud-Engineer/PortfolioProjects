import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
# screen.bgcolor('black')

player = Player()
screen.listen()
screen.onkey(player.move,'Up')
car_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on = False
            score.gameOver()

    # Detect Crossing
    if player.successful_crossing():
        player.go_to_start()
        car_manager.level_up()
        score.update_level()


screen.exitonclick()


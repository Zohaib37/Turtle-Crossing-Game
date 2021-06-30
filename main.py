import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=player.move)

count = 0
game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        car_manager.create_cars()

    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player reaches finish line
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()

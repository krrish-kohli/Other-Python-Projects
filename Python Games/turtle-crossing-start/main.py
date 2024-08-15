import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating player, car_manager and scoreboard objects.
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Using the up arrow key to move the turtle.
screen.listen()
screen.onkey(player.move, "Up")

# Game loop.
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# Creating and moving the cars.
    car_manager.create_cars()
    car_manager.move_cars()

# Displaying the score.
    scoreboard.display_score()

# Detect collisions with the cars.
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            scoreboard.game_over()
            game_is_on = False

# Detect if it reached finish line.
    if player.ycor() > 280:
        player.refresh()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()

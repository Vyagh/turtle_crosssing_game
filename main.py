import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=user.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()    # Not cars but car because it has to generate only one car.
    car_manager.drive_car()

    screen.update()


screen.exitonclick()


# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle
#  north.

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge
#  of the screen. No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle)Hint:generate a new car only every 6th time the game loop runs

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
#  When this happens, return the turtle to the starting position and increase the speed of the cars.
#  Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.

# Detect when the turtle player collides with a car and stop the game if this happens.

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
#  crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.


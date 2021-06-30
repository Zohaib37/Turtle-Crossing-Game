from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

temp_y = 999


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        global temp_y
        car = Turtle("square")
        car.penup()
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        y = random.randrange(-250, 250, 30)
        if y == temp_y:
            y =  random.randrange(-250, 250, 30)
        temp_y = y
        car.goto(300, y)
        car.setheading(180)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


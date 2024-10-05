from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a new car and add it to the list."""
        if random.randint(1, 6) == 1:
            new_car = self._create_new_car()
            self.cars.append(new_car)

    def _create_new_car(self):
        """Initialize a new car with random properties."""
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(300, random.randint(-250, 250))
        return new_car

    def move_cars(self):
        """Move all cars backward based on the current speed."""
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        """Increase the speed of the cars."""
        self.speed += MOVE_INCREMENT

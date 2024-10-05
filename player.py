from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        """Initialize the player turtle with its starting attributes."""
        super().__init__()
        self.setup_player()

    def setup_player(self):
        """Set up the turtle's appearance and initial position."""
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.reset_position()

    def move(self):
        """Move the player forward by the specified distance."""
        self.forward(MOVE_DISTANCE)

    def reached_finish(self):
        """Check if the player has reached the finish line."""
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        """Reset the player's position to the starting point."""
        self.goto(STARTING_POSITION)

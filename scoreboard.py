from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with its initial attributes."""
        super().__init__()
        self.setup_scoreboard()

    def setup_scoreboard(self):
        """Set up the scoreboard's appearance and position."""
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 0
        self.display_level()

    def display_level(self):
        """Display the current level on the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increase the level and update the scoreboard display."""
        self.level += 1
        self.display_level()

    def game_over(self):
        """Display the game over message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        self.screen = Screen()
        self.player = Player()
        self.cars = CarManager()
        self.score = Scoreboard()
        self.is_running = True

        self.setup_screen()
        self.bind_keys()

    def setup_screen(self):
        """Initialize the game screen settings."""
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

    def bind_keys(self):
        """Bind the Up arrow key to the player's move method."""
        self.screen.listen()
        self.screen.onkey(self.player.move, "Up")

    def run(self):
        """Start the main game loop."""
        while self.is_running:
            time.sleep(0.1)
            self.screen.update()
            self.cars.create()
            self.cars.move()

            if self.player.reached_finish():
                self._handle_level_up()

            if self._check_collision():
                self.is_running = False
                self.score.game_over()

        self.screen.exitonclick()

    def _handle_level_up(self):
        """Handle player reaching the finish line."""
        self.player.reset()
        self.score.level_up()
        self.cars.increase_speed()

    def _check_collision(self):
        """Check for collision between the player and cars."""
        for car in self.cars.cars:  # Changed from `cars.all_cars` to `cars.cars`
            if self.player.distance(car) < 20:
                return True
        return False

if __name__ == "__main__":
    game = Game()
    game.run()

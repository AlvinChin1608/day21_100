from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score to 0
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position the scoreboard at the top center
        self.hideturtle()  # Hide the turtle object
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()  # Clear previous score text
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
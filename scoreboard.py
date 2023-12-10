from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over !", align="center", font=("Arial", 24, "bold"))
        self.goto(0, -40)
        self.color("yellow")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "bold"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

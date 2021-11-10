from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15,'normal'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, 'normal'))

    def stop(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 15, 'normal'))





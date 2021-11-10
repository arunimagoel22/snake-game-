from turtle import Turtle

is_game = True
POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]


class SnakeBody:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "RIGHT"

    def create_snake(self):
        for pos in POSITIONS:
            t = Turtle("square")
            t.color("pink")
            t.penup()
            t.goto(pos)
            self.segments.append(t)

    def move_forward(self):
        for each in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[each - 1].xcor()
            next_y = self.segments[each - 1].ycor()
            self.segments[each].goto(next_x, next_y)
        self.segments[0].forward(20)

    def up(self):
        if self.direction != "DOWN":
            self.segments[0].seth(90)
            self.direction = "UP"

    def down(self):
        if self.direction != "UP":
            self.segments[0].seth(270)
            self.direction = "DOWN"

    def right(self):
        if self.direction != "LEFT":
            self.segments[0].seth(0)
            self.direction = "RIGHT"

    def left(self):
        if self.direction != "RIGHT":
            self.segments[0].seth(180)
            self.direction = "LEFT"

    def return_cor(self):
        x = self.segments[0].xcor()
        y = self.segments[0].ycor()
        return x, y

    def increase(self):
        t = Turtle("square")
        t.color("pink")
        t.penup()
        l = len(self.segments) - 1
        x_cor = 0
        y_cor = 0
        if self.direction == "UP":
            x_cor = self.segments[l].xcor()
            y_cor = self.segments[l].ycor() - 20
        if self.direction == "DOWN":
            x_cor = self.segments[l].xcor()
            y_cor = self.segments[l].ycor() + 20
        if self.direction == "RIGHT":
            x_cor = self.segments[l].xcor() - 20
            y_cor = self.segments[l].ycor()
        if self.direction == "LEFT":
            x_cor = self.segments[l].xcor() + 20
            y_cor = self.segments[l].ycor()
        t.goto(x_cor, y_cor)
        self.segments.append(t)

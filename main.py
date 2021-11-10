from turtle import Screen
from snake import SnakeBody
from food import Food
import time
import random
from score_board import ScoreBoard

screen = Screen()
is_game = True
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = SnakeBody()
score = ScoreBoard()
screen.update()
f1 = Food()


def refresh():
    x_cor = random.randint(-299, 299)
    y_cor = random.randint(-299, 299)
    return x_cor, y_cor


# def stop():
#     global is_game
#     is_game = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(stop(), "a")

while is_game:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()

    if f1.distance(snake.return_cor()) < 15:
        f1.goto(refresh())
        score.increase_score()
        snake.increase()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        is_game = False
        score.stop()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 8:
            is_game = False
            score.stop()
screen.exitonclick()

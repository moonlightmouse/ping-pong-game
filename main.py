from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import randint
import time
from animation import motion

screen = Screen()
screen.listen()
screen.tracer(0)

paddle_left = Paddle()
paddle_right = Paddle()
paddle_right.setx(370)

motion(1, 2)

scoreboard = Scoreboard()

ball = Ball()

screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

screen.title ("Пингъ-понгъ для слабонервных")
screen.bgcolor("black")
screen.setup(width=800, height=600)
speed = 0.01


game_is_on = True
while game_is_on:

    time.sleep(speed)
    screen.update()
    ball.forward(5)

    # удар о потолок и пол
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.setheading(360 - ball.heading())

    # удар о ракетки
    if ball.distance(paddle_right) <= 50 and ball.xcor() >= 350 or ball.distance(paddle_left) <= 50 and ball.xcor() <= -360:
        ball.setheading(ball.heading() - 180)
        ball.setheading(360 - ball.heading())
        if speed >= 0.01:
            speed *= 0.4

    # правый пропуск
    if ball.xcor() >= 370:
        ball.goto(0,0)
        ball.setheading(randint(290, 400))
        scoreboard.score_left()

    # левый пропуск
    if ball.xcor() <= -380:
        ball.goto(0,0)
        ball.setheading(randint(120, 250))
        scoreboard.score_right()

screen.exitonclick()


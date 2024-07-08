import time
from turtle import Screen
from django.shortcuts import render, HttpResponse

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

def index(request):
    return HttpResponse("This is for first commit.")


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=900)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((420, 0))
l_paddle = Paddle((-420, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #collision of the ball
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 390 or ball.distance(l_paddle) < 50 and ball.xcor() < -390:
        ball.bounce_x()

    #Detect right paddle misses the ball
    if ball.xcor() > 460:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()

  #left sided paddle miss
    if ball.xcor() < -460:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()



screen.exitonclick()

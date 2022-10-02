from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time, math



# screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)


game_is_on = True
t = 0.05

p1 = Paddle(350, 0)
p2 = Paddle(-350, 0)
b = Ball()
score = ScoreBoard()

while game_is_on:
    
    time.sleep(t)

    # keys to move the paddles
    screen.update()
    screen.onkey(p1.up, "Up")
    screen.onkey(p1.down, "Down")
    screen.onkey(p2.up, "w")
    screen.onkey(p2.down, "s")

    b.move()

    # detect collision with wall
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.bounce_y()
    
    if b.xcor() >= 380 or b.xcor() <= -380:
        b.bounce_x()

    
    # detect collision with paddle
    for s in p1.segments:
        if s.distance(b) <=20:
            t = 0.04
            b.bounce_x()
    
    for s in p2.segments:
        if s.distance(b) <=20:
            t = 0.04
            b.bounce_x()


    # check goal
    if b.xcor() >= 370:
        score.update_l_score()
        b.restart()
        t = 0.05
        # game_is_on = False
    if b.xcor() <= -370:
        score.update_r_score()
        b.restart()
        t = 0.05


screen.exitonclick()
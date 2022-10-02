
from turtle import Turtle


class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.segments = []
        self.make_paddle(x, y)




    # paddles of 5 squares
    def make_paddle(self, x, y):
        for i in range(5):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(x, y)
            self.segments.append(segment)
            y-=20


    # up movement
    def up(self):
        if self.segments[0].ycor() <= 270 and self.segments[-1].ycor() >= -270:
            head = self.segments[0]
            head.setheading(90)
            for i in range(len(self.segments)-1, 0, -1):
                x = self.segments[i].xcor()
                y = self.segments[i].ycor()+20
                self.segments[i].goto(x, y)
            head.forward(20)

    # down movement
    def down(self):
        if self.segments[0].ycor() <= 270 and self.segments[-1].ycor() >= -270:
            head = self.segments[0]
            head.setheading(90)
            for i in range(len(self.segments)-1, 0, -1):
                x = self.segments[i].xcor()
                y = self.segments[i].ycor()-20
                self.segments[i].goto(x, y)
            head.backward(20)
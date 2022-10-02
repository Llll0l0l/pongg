from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 180)
        self.hideturtle()
        self.write("0      0", align="center", font=("Courier", 80, "normal"))
        self.l_score = 0
        self.r_score = 0


    def update_l_score(self):
        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score}      {self.r_score}", align="center", font=("Courier", 80, "normal"))
        
    

    def update_r_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.l_score}      {self.r_score}", align="center", font=("Courier", 80, "normal"))
        
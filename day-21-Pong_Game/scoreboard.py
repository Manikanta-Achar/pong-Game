from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update()

    def score_line(self):
        tom = Turtle()
        tom.color("white")
        tom.setheading(90)
        tom.hideturtle()
        tom.penup()
        tom.forward(300)
        tom.pendown()
        tom.setheading(270)
        tom.pensize(10)
        tom.forward(600)


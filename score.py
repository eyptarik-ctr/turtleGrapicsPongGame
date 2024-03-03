from turtle import Turtle

class Score :
    def __init__(self):
        self.score_r = 0
        self.score_l = 0

    def right_score(self):
        self.r_score = Turtle()
        self.r_score.penup()
        self.r_score.hideturtle()
        self.r_score.sety(270)
        self.r_score.setx(50)
        self.r_score.color('white')
        self.r_score.write(f'{self.score_r}', font=('ariel', 50, 'bold'))
    def left_score(self):
        self.l_score = Turtle()
        self.l_score.penup()
        self.l_score.hideturtle()
        self.l_score.color('white')
        self.l_score.sety(270)
        self.l_score.setx(-70)
        self.l_score.write(f'{self.score_l}', font=('ariel', 50, 'bold'))

    def increase_r(self):
        self.score_r += 1
        self.r_score.clear()
        self.r_score.write(f'{self.score_r}', font=('ariel', 50, 'bold'))

    def increase_l(self):
        self.score_l += 1
        self.l_score.clear()
        self.l_score.write(f'{self.score_l}', font=('ariel', 50, 'bold'))
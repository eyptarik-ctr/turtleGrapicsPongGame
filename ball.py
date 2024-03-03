from turtle import Turtle
from random import *

import score
from score import *
class Ball:
    def __init__(self):
        self.is_game_on = True
        self.ball_body = []
        self.ball()
        self.draw_circle()
        self.move()
    def ball(self):
        cannon = Turtle()
        cannon.shape('circle')
        cannon.color('white')
        cannon.penup()
        cannon.speed('fastest')
        cannon.sety(randint(-300, 300))
        cannon.speed(3)
        cannon.setheading(randint(120, 230))
        self.ball_body.append(cannon)
    def spilit_to_screen(self):
        line = Turtle()
        line.hideturtle()
        line.color('white')
        line.penup()
        line.speed('fastest')
        line.setheading(270)
        line.sety(540)
        for i in range(1,60):
            line.pendown()
            line.forward(10)
            line.penup()
            line.forward(10)
    def draw_circle(self):
        round = Turtle()
        round.hideturtle()
        round.color('white')
        round.speed('fastest')
        round.penup()
        round.sety(-50)
        round.pendown()
        round.circle(50)

    def reflect(self):
        if self.ball_body[0].ycor() > 340:
            self.ball_body[0].setheading(360 - self.ball_body[0].heading() + randint(-10, 10))
        elif self.ball_body[0].ycor() < -340:
            self.ball_body[0].setheading(360 - self.ball_body[0].heading() + randint(-10, 10))
        elif self.ball_body[0].xcor() < -620:
            self.is_game_on = False
            self.ball_body[0].hideturtle()
            self.__init__()
        elif self.ball_body[0].xcor() > 620:
            self.is_game_on = False
            self.ball_body[0].hideturtle()
            self.__init__()
    def move(self):
        self.ball_body[0].forward(5)

    def reflect_to_board(self):
        self.ball_body[0].setheading(180 - self.ball_body[0].heading() + randint(-10, 10))

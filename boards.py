from turtle import Turtle

class Boards:
    def __init__(self):
        self.y_coordinates = [60, 40, 20, 0, -20, -40, -60]
        self.board_r_segments = []
        self.board_l_segments = []
        self.board_right()
        self.board_left()
    def board_right(self):
        for _ in self.y_coordinates:
            new_r = Turtle()
            new_r.speed('fastest')
            new_r.shape('square')
            new_r.setheading(90)
            new_r.penup()
            new_r.sety(_)
            new_r.setx(620)
            new_r.color('white')
            self.board_r_segments.append(new_r)

    def r_board_up(self):
        if self.board_r_segments[0].ycor() < 320:
            for _ in range(0, 7):
                self.board_r_segments[_].forward(105)

    def r_board_down(self):
        if self.board_r_segments[0].ycor() > -200:
            for _ in range(0, 7):
                self.board_r_segments[_].backward(105)

    def board_left(self):
        for _ in self.y_coordinates:
            new_l = Turtle()
            new_l.speed('fastest')
            new_l.shape('square')
            new_l.setheading(90)
            new_l.penup()
            new_l.sety(_)
            new_l.sety(_)
            new_l.setx(-620)
            new_l.color('white')
            self.board_l_segments.append(new_l)

    def l_board_up(self):
        if self.board_l_segments[0].ycor() < 300:
            for _ in range(0, 7):
                self.board_l_segments[_].forward(105)

    def l_board_down(self):
        if self.board_l_segments[0].ycor() > -200:
            for _ in range(0, 7):
                self.board_l_segments[_].backward(105)



from turtle import Screen
from ball import *
from boards import *
from score import Score
from time import *
import threading
window = Screen()
window.tracer(0)
window.setup(width=1280, height=720)
window.bgcolor('black')
window.listen()
board = Boards()
cannon = Ball()
cannon.spilit_to_screen()
scorees = Score()
scorees.right_score()
scorees.left_score()
window.onkey(fun=board.r_board_up, key='Up')
window.onkey(fun=board.r_board_down, key='Down')
window.onkey(fun=board.l_board_up, key='w')
window.onkey(fun=board.l_board_down, key='s')
while cannon.is_game_on:
    window.update()
    sleep(0.01)
    cannon.reflect()
    cannon.move()
    if cannon.ball_body[0].xcor() < -620:
        scorees.increase_r()
    elif cannon.ball_body[0].xcor() > 620:
        scorees.increase_l()
    for _ in range(0, 7):
        if cannon.ball_body[0].distance(board.board_l_segments[_]) < 10:
            cannon.reflect_to_board()
        elif cannon.ball_body[0].distance(board.board_r_segments[_]) < 10:
            cannon.reflect_to_board()

window.mainloop()
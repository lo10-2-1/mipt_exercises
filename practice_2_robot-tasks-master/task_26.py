#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def cross():
        move_right()
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    
    for i in range(5):
        for j in range(4):
            cross()
            if j<3:
                move_down(n=4)
            else:
                move_right(n=4)
        for h in range(4):
            cross()
            if h<3:
                move_up(n=4)
            elif i==4 and wall_is_above():
                break
            else:
                move_right(n=4)
    
    move_down(n=16)

    for k in range(10):
        cross()
        if k<9:
            move_left(n=4)


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for j in range(1, 13):
        if j%2==1:
            move_right()
            for i in range(2,29):
                fill_cell()
                move_right()
            move_down()
        else:
            move_left()
            for i in range(2,29):
                fill_cell()
                move_left()
            move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()

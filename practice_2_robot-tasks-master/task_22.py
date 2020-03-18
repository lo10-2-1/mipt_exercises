#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while wall_is_beneath() is False:
        while wall_is_on_the_right() is False:
            fill_cell()
            move_right()
        fill_cell()
        if wall_is_beneath():
            break
        move_down()
        while wall_is_on_the_left() is False:
            fill_cell()
            move_left()
        fill_cell()
        if wall_is_beneath():
            break
        move_down()
    if cell_is_filled() is False:
        while wall_is_on_the_right() is False:
            fill_cell()
            move_right()
        fill_cell()
        while wall_is_on_the_left() is False:
            move_left()


if __name__ == '__main__':
    run_tasks()

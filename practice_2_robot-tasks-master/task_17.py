#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    if wall_is_beneath():
        while cell_is_filled() is False:
            move_up()
    move_right()
    if cell_is_filled() is False:
        move_left(n=2)


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while wall_is_on_the_right() is False:
        if wall_is_beneath() and wall_is_above() is False:
            fill_cell()
        move_right()
    if wall_is_beneath() and wall_is_above() is False:
        fill_cell()


if __name__ == '__main__':
    run_tasks()
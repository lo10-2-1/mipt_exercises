#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while wall_is_beneath():
        if wall_is_above() is False:
            fill_cell()
        if wall_is_on_the_right() is False:
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()
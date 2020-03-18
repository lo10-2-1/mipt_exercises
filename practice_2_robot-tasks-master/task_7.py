#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath() is False:
        move_down()
    while wall_is_beneath() is True:
        move_right()
    move_down()
    move_left()
    while wall_is_above() is True:
        if wall_is_on_the_left() is True:
            break
        else:
            move_left()


if __name__ == '__main__':
    run_tasks()

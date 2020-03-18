#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    while wall_is_on_the_right() is False:
        move_right()
        if wall_is_above() is False:
            move_up()
            break
    while wall_is_on_the_left() is False:
        move_left()
        if wall_is_above() is False:
            move_up()
            break
    while wall_is_above() is False:
        move_up()
    while wall_is_on_the_left() is False:
        move_left()


if __name__ == '__main__':
    run_tasks()

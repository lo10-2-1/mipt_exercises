#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_beneath():
        while wall_is_above() is False:
            move_up()
    elif wall_is_above():
        while wall_is_beneath() is False:
            move_down()
    if wall_is_on_the_left():
        while wall_is_on_the_right() is False:
            move_right()
    elif wall_is_on_the_right():
        while wall_is_on_the_left() is False:
            move_left()


if __name__ == '__main__':
    run_tasks()

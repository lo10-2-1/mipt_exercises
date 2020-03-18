#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above() is False:
        move_up()
    elif wall_is_beneath() is False:
        move_down()
    elif wall_is_on_the_left() is False:
        move_left()
    else:
        move_right()

if __name__ == '__main__':
    run_tasks()

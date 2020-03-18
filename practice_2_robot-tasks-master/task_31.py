#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    def movetothewall(n):
        if wall_is_beneath() is False:
            move_down()
            n = 2
        elif wall_is_on_the_left() or wall_is_on_the_right():
            n -= 1
        return n

    paths=2

    while paths>0:
        if wall_is_beneath():
            while wall_is_on_the_right() is False:
                move_right()
                paths=movetothewall(paths)

            while wall_is_on_the_left() is False:
                move_left()
                paths=movetothewall(paths)
        else:
            move_down()

if __name__ == '__main__':
    run_tasks()

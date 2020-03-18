#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    threecells=0

    while wall_is_on_the_right() is False:
        if cell_is_filled():
            threecells+=1
            if threecells==3:
                break
            move_right()
        else:
            threecells=0
            move_right()

if __name__ == '__main__':
    run_tasks()

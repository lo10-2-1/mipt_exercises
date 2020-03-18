#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    allcells=0

    while wall_is_on_the_right() is False:
        move_right()
        if cell_is_filled():
            allcells+=1
        if allcells==5:
            break


if __name__ == '__main__':
    run_tasks()

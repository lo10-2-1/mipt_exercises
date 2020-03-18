#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    step=1
    move_right(n=1)

    while wall_is_on_the_right() is False:
        fill_cell()
        for i in range(step):
            if wall_is_on_the_right() is False:
                move_right()
            else:
                break
        step+=1


if __name__ == '__main__':
    run_tasks()

#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while True:
        if wall_is_beneath() is False and wall_is_above() is False:
            move_up()
            fill_cell()
            move_down(n=2)
            fill_cell()
            move_up()
        elif wall_is_beneath() and wall_is_above() is False:
            move_up()
            fill_cell()
            move_down()
        elif wall_is_above() and wall_is_beneath() is False:
            move_down()
            fill_cell()
            move_up()
        elif wall_is_above() and wall_is_beneath():
            fill_cell()

        if wall_is_on_the_right():
            break
        
        move_right()    


if __name__ == '__main__':
    run_tasks()

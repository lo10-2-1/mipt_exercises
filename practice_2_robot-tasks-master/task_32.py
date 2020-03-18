#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_18():
    filledcells=0

    while wall_is_on_the_right() is False:
        if wall_is_above() and wall_is_beneath():
            fill_cell()
            move_right()
            if wall_is_on_the_right():
                break
        elif wall_is_above() is False:
            while wall_is_above() is False:
                move_up()
                if cell_is_filled():
                    filledcells+=1
                fill_cell()
            while wall_is_beneath() is False:
                move_down()
                if wall_is_beneath():
                    move_right()
                    break
    
    mov('ax', filledcells)


if __name__ == '__main__':
    run_tasks()

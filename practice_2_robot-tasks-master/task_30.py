#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():

    def line_left(n):
        move_left()
        for i in range(n):
            fill_cell()
            move_left()
    
    def line_up(n):
        move_up()
        for i in range(n):
            fill_cell()
            move_up()

    def line_right(n):
        move_right()
        for i in range(n):
            fill_cell()
            move_right()
    
    def line_down(n):
        move_down()
        for i in range(n):
            fill_cell()
            move_down()

    line=0
    move_down()

    while wall_is_beneath() is False:
        fill_cell()
        move_down()
        line+=1
    
    while line>=1:
        line_up(line)
        line_right(line)
        line_down(line)
        line_left(line)
        line-=2
        if line>=1:
            move_up()
            move_right()
        else:
            break

    
    while wall_is_beneath() is False:
        move_left()
        move_down()
                

            



if __name__ == '__main__':
    run_tasks()

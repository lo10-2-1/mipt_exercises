#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def cross():
        move_down()
        move_right(n=2)
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_up()
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    
    cross()



if __name__ == '__main__':
    run_tasks()

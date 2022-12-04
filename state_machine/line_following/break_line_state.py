from state import State
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

class BreakLineState(State):
    def run(self, robot, motor_left, motor_right, color_sensor, gyro_sensor, context):
        robot.drive(40, 0)
        wait(1000)
        robot.stop()
        from search_line_state import SearchLineState
        context.set_state(SearchLineState())
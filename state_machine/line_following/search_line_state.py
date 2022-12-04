from state import State
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

class SearchLineState(State):
    def search_line(motor1,  motor2, color_sensor):
        start_tacho = motor1.angle()
        motor1.run(100)
        motor2.run(-50)
        while True:
            if found_line(color_sensor):
                motor1.stop()
                motor2.stop()
                return True
            elif turn_robot(start_tacho, motor1):
                motor1.stop()
                motor2.stop()
                while motor1.angle() >= start_tacho:
                    motor1.run(-100)
                    motor2.run(-50)
                motor1.stop()
                motor2.stop()
                return False
        
    def found_line(color_sensor):
        if color_sensor.reflection() < threshold:
            return True
        return False

    def turn_robot(start_tacho, motor):
        if motor.angle() > start_tacho + 600:
            return True
        return False

    def run(self, robot, motor_left, motor_right, color_sensor, gyro_sensor, context):
        search_left = search_line(motor_right, motor_left, color_sensor)
        wait(1000)
        if not search_left:
            search_right = search_line(motor_left, motor_right, color_sensor)
            wait(1000)
        if search_left or search_right:
            from pid_state import PidState
            context.set_state(PidState())
        else:
            from break_line_state import BreakLineState
            context.set_state(BreakLineState())
        
        
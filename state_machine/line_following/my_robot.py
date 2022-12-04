import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from context import Context

from end_state import EndState
from search_line_state import SearchLineState
from pid_state import PidState
from break_line_state import BreakLineState
from state import State

# EV3 init

def main():
    ev3 = EV3Brick()
    motor_left = Motor(Port.A)
    motor_right = Motor(Port.B)
    robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=152)
    #robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

    color_sensor = ColorSensor(Port.S1)
    #obstacle_sensor = UltrasonicSensor(Port.S2)
    gyro_sensor= GyroSensor(Port.S3)

    motorC = Motor(Port.C) # Magnet\
        
    pid = PidState()
    start_state = pid
    context = Context(start_state)


    while True:
        if context.get_state().__class__.__name__ == 'EndState':
            context.run(robot, motor_left, motor_right, color_sensor, gyro_sensor)
            break
        context.run(robot, motor_left, motor_right, color_sensor, gyro_sensor)
    
if __name__ == '__main__':
    main()
    

    
    
    

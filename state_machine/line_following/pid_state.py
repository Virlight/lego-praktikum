from state import State
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

BLACK = 0
WHITE = 100
SPEED = 60
threshold = (BLACK + WHITE) / 2

PROPORTIONAL_GAIN = 2.2
INTEGRAL_GAIN = 0.11
DERIVATIVE_GAIN = 0.7
MAX_BLACK_TIME = 0.06


class PidState(Sate):
    def run(self, robot, motor_left, motor_right, color_sensor, gyro_sensor, context):
        integral = 0
        derivative = 0
        lastError = 0
        black_time = 0
        black_angle = 0
        time_start = 0
        turn_rate = 0
        on_line = True
        while not color_sensor.color() is Color.BLUE:
            if black_time < MAX_BLACK_TIME:
                #PID  
                error = threshold - color_sensor.reflection()
                integral = integral + error
                derivative = error - lastError
                turn_rate = PROPORTIONAL_GAIN * error + INTEGRAL_GAIN * integral + DERIVATIVE_GAIN * derivative
                motor_left.run(SPEED - turn_rate)
                motor_right.run(SPEED + turn_rate) 
                lastError = error
                
                if color_sensor.reflection() != BLACK:
                    gyro_sensor.reset_angle(0)
                    black_time = 0 
                    on_line = True
                elif not on_line:
                    time_end = time.time()
                    black_time += time_end - time_start
                    print('black_time:', black_time)
                else:
                    time_start = time.time() 
                    on_line = False
                
                    
            else:
                while gyro_sensor.angle() < 0:
                    motor_left.run(-1 * (SPEED - turn_rate))
                    motor_right.run(-1 * (SPEED + turn_rate))
                motor_left.stop()
                motor_right.stop()
                wait(100)
                from search_line_state import SearchLineState
                context.set_state(SearchLineState())
                return
        from end_state import EndState
        context.set_state(EndState())
    
        
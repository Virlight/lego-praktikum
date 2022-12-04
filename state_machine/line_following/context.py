#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from pid_controller import pid

# EV3 init

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)
#touch_sensor = TouchSensor(Port.S2)
gyro = GyroSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter = 55.5, axle_track = 104)

pid(robot, color_sensor)


if __name__ == '__main__':
    main()
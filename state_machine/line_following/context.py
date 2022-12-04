#!/usr/bin/env pybricks-micropython

class Context():
    def __init__(self, state):
        self.state = state
    
    def run(self, robot, motor_left, motor_right, color_sensor, gyro_sensor):
        self.state.run(robot, motor_left, motor_right, color_sensor, gyro_sensor, self)
        
    def set_state(self, new_state):
        self.state = new_state
        
    def get_state(self):
        return self.state




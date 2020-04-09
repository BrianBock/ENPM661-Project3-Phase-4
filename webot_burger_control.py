from controller import Robot, DistanceSensor, Motor
import time
import os
import numpy as np
import math


Fast=2
Slow=1
moveTime=3
path_file='path_file-s(895, 1600, 90)-g(5000, 1600)-2,1-t3.npz'


def move(moveTime, TIME_STEP, leftSpeed,rightSpeed):
        # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
    # robot.step(moveTime*1000/timestep)
    robot.step(moveTime*1000)

    leftMotor.setVelocity(0)
    rightMotor.setVelocity(0)

    robot.step(50)



MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()
print("Robot created")

# initialize devices
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
print("Wheel configured")

# time in [ms] of a simulation step
timestep = int(robot.getBasicTimeStep())
print(timestep)

# feedback loop: step simulation until receiving an exit event
# while robot.step(timestep) != -1:

# initialize motor speeds at 50% of MAX_SPEED.
# leftSpeed  = 0.5 * MAX_SPEED
# rightSpeed = 0.5 * MAX_SPEED

# Load the save file from Phase 3
if os.path.exists(path_file):
    with np.load(path_file) as data:
        action_list = data['path_moves']
else:
    print("Unable to import '"+path_file+"'. Please check that this file exists and then restart this program.")
    exit()

# action_list=['FastFast','FastSlow','SlowFast']


    #action_list is an ordered list of actions
for i,direction in enumerate(action_list):
    print(direction)
    if direction == "FastFast":
        ul=Fast
        ur=Slow
    elif direction == "FastSlow":
        ul=Fast
        ur=Slow
    elif direction == "Fast0":
        ul=Fast
        ur=0
    elif direction == "SlowFast":
        ul=Slow
        ur=Fast
    elif direction == "SlowSlow":
        ul=Slow
        ur=Slow
    elif direction == "Slow0":
        ul=Slow
        ur=0
    elif direction == "0Fast":
        ul=0
        ur=Fast
    elif direction == "0Slow":
        ul=0
        ur=Slow

    # Drive the Robt
    print(i)
    move(moveTime,timestep,ul, ur)
    

print("done")



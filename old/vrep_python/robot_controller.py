# Make sure to have the server side running in V-REP: 
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')
    exit()

import time
import os
import numpy as np
import math


Fast=2
Slow=1
moveTime=3
path_file='../path_file-s(895, 1600, 90)-g(5000, 1600)-2,1-t3.npz'




def move(package, left_speed, right_speed):

    clientID=package[0]
    vrep=package[1]
    Turtle_Right_Wheel=package[2]
    Turtle_Left_Wheel=package[3]
    moveTime=package[4]

    # spin wheels
    vrep.simxSetJointTargetPosition(clientID,Turtle_Right_Wheel,5000,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetPosition(clientID,Turtle_Left_Wheel,5000,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,right_speed,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,left_speed,vrep.simx_opmode_oneshot)

    # rV=vrep.simxGetJointVelocity(clientID,Turtle_Right_Wheel,vrep.simx_opmode_oneshot)
    # lV=vrep.simxGetJointVelocity(clientID,Turtle_Left_Wheel,vrep.simx_opmode_oneshot)

    # print(rV,lV)
    
    time.sleep(moveTime)
    
    # stop wheels
    vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,0,vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,0,vrep.simx_opmode_oneshot)
    time.sleep(.1);







# Connect to V-REP
print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')

    # Get Object Handles for All Parts
    [x, Turtle_Right_Wheel]=vrep.simxGetObjectHandle(clientID, 'wheel_right_joint', vrep.simx_opmode_blocking);
    [x, Turtle_Left_Wheel]=vrep.simxGetObjectHandle(clientID, 'wheel_left_joint', vrep.simx_opmode_blocking); 

    package=(clientID,vrep,Turtle_Right_Wheel,Turtle_Left_Wheel,moveTime)





    

    # Load the save file from Phase 3
    if os.path.exists(path_file):
        with np.load(path_file) as data:
            action_list = data['path_moves']
    else:
        print("Unable to import '"+path_file+"'. Please check that this file exists and then restart this program.")
        exit()

        #action_list is an ordered list of actions
    for direction in action_list:
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
        move(package, ul, ur)
        # vrep.simxCallScriptFunction(package,ul,ur)

    # # Drive the Robot
    # move(package, Fast,Fast)
    # move(package, Fast,Slow)
    # move(package, Fast,0)


    # time.sleep(1)
    # move(package, Slow,Fast)
    # move(package, Slow,Slow)
    # move(package, Slow,0)





# The remote API client application would then call above script function in following manner (e.g. via a Python script):

# inputInts=[1,2,3]
# inputFloats=[53.21,17.39]
# inputStrings=['Hello','world!']
# inputBuffer=bytearray()
# inputBuffer.append(78)
# inputBuffer.append(42)
# res,retInts,retFloats,retStrings,retBuffer=sim.simxCallScriptFunction(clientID,'objectName',sim.sim_scripttype_childscript,
#                 'myFunctionName',inputInts,inputFloats,inputStrings,inputBuffer,sim.simx_opmode_blocking)
# if res==sim.simx_return_ok:
#     print (retInts)
#     print (retFloats)
#     print (retStrings)
#     print (retBuffer)




    # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')
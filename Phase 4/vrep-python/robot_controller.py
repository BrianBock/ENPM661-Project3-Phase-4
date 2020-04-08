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

import time
from move import move

Fast=15
Slow=5
moveTime=1

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




    # Drive the Robot
    move(package, Fast,Fast)
    move(package, Fast,Slow)
    move(package, Fast,0)


    time.sleep(1)
    move(package, Slow,Fast)
    move(package, Slow,Slow)
    move(package, Slow,0)








    # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')

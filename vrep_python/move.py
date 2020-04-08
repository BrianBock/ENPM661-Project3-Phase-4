import time

def move(package, left_speed, right_speed):

	clientID=package[0]
	vrep=package[1]
	Turtle_Right_Wheel=package[2]
	Turtle_Left_Wheel=package[3]
	moveTime=package[4]

	# spin wheels
	x=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,right_speed,vrep.simx_opmode_blocking);
	x=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,left_speed,vrep.simx_opmode_blocking);
	
	time.sleep(moveTime)
	
	# stop wheels
	x=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,0,vrep.simx_opmode_blocking);
	x=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,0,vrep.simx_opmode_blocking);
	time.sleep(.5);

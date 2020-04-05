# Import Python functions
import cv2 
from datetime import datetime as dtime

# Import our classes
from maze import Maze
from robot import Robot

# Visualization and Video
write_to_video = True
show_visualization = False
show_solve=False #show every step of the solution to the video/visualization (if True)

# Allow for user input start/goal coordinates, wheel speeds, and move time
userInput = False

# Precomputed Saves
trySolve=True #Toggle False if you want to use a precomputed save




# Construct maze object
maze = Maze('maze.txt')
print("Maze created")

# Contstruct the robot
robot = Robot(maze,userInput)
print("Robot created")

# Record the start time so we can compute run time at the end
starttime = dtime.now()

if trySolve:
	# Run Search
	print("Attempting to solve. Please be patient, this may take several minutes")
	robot.A_star()

	if robot.foundGoal:
	    searchtime=dtime.now()
	    searchtime=searchtime-starttime
	    print('Found solution in '+str(searchtime)+' (hours:min:sec)')
	    print('Generating path')
	    robot.generate_path()
	    print('Path generated')

	else:
	    print('Unable to find path between start and goal.')
	    exit()


# Visualize the path
robot.visualize(write_to_video,show_visualization,show_solve)
endtime = dtime.now()
runtime=endtime-starttime
print("Finished in "+str(runtime)+" (hours:min:sec)")



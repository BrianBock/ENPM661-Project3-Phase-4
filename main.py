# Import Python functions
import cv2 
from datetime import datetime as dtime

# Import our classes
from maze import Maze
from robot import Robot

write_to_video = True
show_visualization = False
userInput = False

# Construct maze object
maze = Maze('maze.txt')
print("Maze created")

# Contstruct the robot
robot = Robot(maze,userInput)
print("Robot created. Attempting to solve.")

# Record the start time so we can compute run time at the end
starttime = dtime.now()

# Run Search
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
robot.visualize(write_to_video,show_visualization)
endtime = dtime.now()
runtime=endtime-starttime
print("Finished in "+str(runtime)+" (hours:min:sec)")



# Import Python functions
import cv2 
import numpy as np
import time
from datetime import datetime as dtime
# Import our functions
from maze import Maze
from robot import PointRobot
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection


write_to_video = False
show_visualization = False
userInput = False
search_type = 'A' # D for Dijkstra, B for BFS, A for A*
stepsize = 10 #controls the number of nodes shown in each frame of visualization

# Record the start time so we can compute run time at the end
starttime = dtime.now()

# Construct maze object
maze = Maze('maze2.txt')
print("Maze created")

# Contstruct the robot
robot = PointRobot(maze,userInput)
print("Robot created")

# Run Search
if search_type == 'D':
    robot.Dijkstra()
if search_type == 'B':
    robot.BFS()
if search_type == 'A':
    robot.A_star()


if robot.foundGoal:
    print('Found Path')
    robot.generate_path()

else:
    print('The goal could not be found')
    exit()

# Visualize the path
robot.visualize(show_visualization,write_to_video,stepsize)
endtime = dtime.now()
runtime=endtime-starttime
print("Finished in "+str(runtime)+" (hours:min:sec)")
plt.show()

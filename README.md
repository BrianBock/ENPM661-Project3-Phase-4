# ENPM661 Project 3 Phase 4 - Simulation

## Introduction

This project continues the work done in [ENPM661 Project 3 Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3). In that project, we used A* to find the optimal path through a Cartesian maze with obstacles for a rigid robot. The maze was 10200x10200 mm with 8 obstacles - 4 circles, 3 squares, and a hollow rectangle at the border.

![maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/maze.png)

In this project, we simulate the Turtlebot 2 driving through the 3D version of this maze in Webots. The Turtlebot 2 is a two wheeled differential drive robot. It has 8 possible movements, defined by a combination of 3 speeds for the left and right wheels (user defined Fast, Slow, and 0). 

![V-Rep maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/phase4_webots.png)

There are two start and goal configurations (coordinates are in Cartesian coordinates):

Start: (895,1600), Goal: (5000, 1600)

Start: (1035, 700), Goal: (9300, 7600)

This project was built in Webots.<!--  v3.6.2 (the version that predates the CoppeilaSim rebrand). Python communicates with V-Rep over the [V-Rep remote API](https://www.coppeliarobotics.com/helpFiles/en/remoteApiClientSide.htm). You may need to add the `remote.Api.dll`, or `remoteApi.so` file frmo your install of V-Rep to run this program, depending on your platform. This version has been built to run on macOS 10.15. -->

## Dependencies 

    V-Rep v3.6.2
    Python 3.7


## Instructions for Running the Program - Phase 3
Clone this repository. 
Open the `vrep_sim.ttt` file with V-Rep. Hit the Purple play icon in the top menu bar to start the simulation. Once the simulation is running, open a new terminal window and navigate to the cloned Phase 4 directory. Type `python main.py`, if you have additional older versions of python installed you may need to run `python3` instead. If you try to launch the python file before the simulation runs, it will not work. 

The program will prompt you for a coordinate system. You have 3 choices - image coordinates have the origin at the top left, with positive y in the downward direction, and positive x in the rightward direction. Cartesian coordinates have the origin in the bottom left, with positive y in the upward direction, and positive x in the rightward direction. Gazebo coordinates have the origin at the center, with positive y in the upward direction, and positive x in the rightward direction. Regardless of your coordinate system choice, the output visualizaion will be shown in Cartesian coordinates. 

Once you have selected a coordinate system, you'll be prompted to enter a start point, goal point, and the fast and slow speeds for the robot's wheels. If the points are valid and a solution is possible, the program will solve then show the visualization of the solution. This mode treats your robot as a circle with the given radius and expands all of the obstacles by the radius and clearance.

<!-- In our tests, the program usually solves the path 5-35 minutes (depending on all the run parameters, worst case - 6 hours, 51 min), but can take much longer to export the visualization/video.  -->


## Pre-Computed Solves
When the program finishes solving the path, it saves all of the relevant solution information to a file in the `Solve Files` directory (which is the first reason why you must have write privileges to the directory you save this repo to). The file name for each solution file details that run's parameters. For example: 

`path_file-s(1100, 1000, 90)-g(9000, 9000)-8,1-t1.npz`

Start: (1100, 1000, 90)

Goal: (9000, 9000)

Fast Speed: 8

Slow Speed: 1

Move Time: 1

We ran several different goal configurations and saved them to these files. This allows the solution to be computed independent of visualization. Some of these solutions took several hours to compute. With the solution saved, we can run the visualization at a later time. 

To make use of one of these pre-solved solutions, please follow the following steps:
1. Use the file name of the solution to get the run parameters (as shown above)
2. Enter those parameters in the Init section of `robot.py`. The numbers must exactly match.
3. In the top of `main.py`, toggle `trySolve` to False. 
4. Run `main.py`. 





## Videos




## Github

You can view all of the code related to this project on our Github: https://github.com/BrianBock/ENPM661-Project3-Phase-4

# ENPM661 Project 3 Phase 4 - Simulation

## Introduction

This project continues the work done in [ENPM661 Project 3 Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3). In that project, we used A* to find the optimal path through a Cartesian maze with obstacles for a rigid robot. The maze was 10200x10200 mm with 8 obstacles - 4 circles, 3 squares, and a hollow rectangle at the border.

![maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/maze.png)

In this project, we simulate the Turtlebot 3 Burger driving through the 3D version of this maze in Webots. The Burger is a two wheeled differential drive robot. It has 8 possible movements, defined by a combination of 3 speeds for the left and right wheels (user defined Fast, Slow, and 0). According to the [Burger specifications](http://emanual.robotis.com/docs/en/platform/turtlebot3/specifications/) the max wheel speed of the Bruger is 2.84 rad/s.

![Webots maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/phase4_webots.png)


There are two start and goal configurations (coordinates are in Cartesian coordinates):

Start: (895,1600), Goal: (5000, 1600)

Start: (1035, 700), Goal: (9300, 7600)

This project was built in Webots.


## Instructions for Running the Program - Phase 4

This project utilizes solution files exported from our [Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3). We've included the solution files required for the two start/goal configurations for this project. If you would like to try a different start and goal configuration, there are instructions on how to do so below.


## Trying Different Start/Goal/Speed Configurations
Read the [Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3) documentation to understand how to set your desired parameters. When that is configured the way you'd like, run Phase 3 to export a new solution file. Copy that solution file to `webots_project\controllers\burger_controller\`. You'll see other save files in that same folder. Open `burger_controller.py` (our own Turtlebot3 Burger robot control script) and edit the `path_file` to match the name of the new save file. Save and close the Python file. Open the Webots world. The start position of the Burger is defined in Webots, not Python. Select the Turtlebot3 on the side menu, and adjust it's position to wherever you want it. 

[Change Burger Start](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/changeturtlestart.gif) 





## Videos




## Github

You can view all of the code related to this project on our Github: https://github.com/BrianBock/ENPM661-Project3-Phase-4

# ENPM661 Project 3 Phase 4 - Simulation

## Introduction

This project continues the work done in [ENPM661 Project 3 Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3). In that project, we used A* to find the optimal path through a Cartesian maze with obstacles for a rigid robot. The maze was 10200x10200 mm with 8 obstacles - 4 circles, 3 squares, and a hollow rectangle at the border.

![maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/maze.png)

In this project, we simulate the Turtlebot 3 Burger driving through the 3D version of this maze in Webots. The Burger is a two wheeled differential drive robot. It has 8 possible movements, defined by a combination of 3 speeds for the left and right wheels (user defined Fast, Slow, and 0). According to the [Burger specifications](http://emanual.robotis.com/docs/en/platform/turtlebot3/specifications/) the max wheel speed of the Bruger is 2.84 rad/s.

![Webots maze](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/phase4_webots.png)


There are two start and goal configurations (coordinates are in Cartesian coordinates):

Start: (895,1600), Goal: (5000, 1600)

Start: (1035, 700), Goal: (9300, 7600)

This project was built in [Webots](https://cyberbotics.com/).


## Instructions for Running the Program - Phase 4

Download and install Webots from https://cyberbotics.com/#download. Navigate to either `\webots_project\worlds\phase4_1.wbt` or  `\webots_project\worlds\phase4_2.wbt` and open that file in Webots. When the world has finished loading, hit the grey play button in the center of the top menu bar to play the simulation. You can watch the simulation run in near-real time, or use the button to the right of the play button to speed up the simulation. 


This project utilizes solution files exported from our [Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3). We've included the solution files required for the two start/goal configurations for this project. If you would like to try a different start and goal configuration, there are instructions on how to do so in the section below. 


## Trying Different Start/Goal/Speed Configurations
Read the [Phase 3](https://github.com/BrianBock/ENPM661-Project3-Phase-3) documentation to understand how to set your desired parameters. When that is configured the way you'd like, run Phase 3 to export a new solution file. Copy that solution file to `webots_project\controllers\burger_controller\`. You'll see other save files in that same folder. Open `burger_controller.py` (our own Turtlebot3 Burger robot control script) and edit the `path_file` to match the name of the new save file. Save and close the Python file. Open the Webots world. The start position of the Burger is defined in Webots, not Python. Select the Turtlebot3 on the side menu, and adjust it's position to wherever you want it. 

![Change Burger Start](https://github.com/BrianBock/ENPM661-Project3-Phase-4/blob/master/Images/changeturtlestart.gif) 



Minor positioning errors compound over long sequences of moves, causing the second video to have siginifcant positional errors. 

## Videos

Video 1 (Angled view) - https://youtu.be/_ZxGPbN_xco

Video 1 (Top View) - https://youtu.be/LnL1jkQIxTE

Minor errors (not noticable in the short sequence of video 1) compound over long sequences of moves, causing the second video to have siginifcant positional errors. 

Video 2 - https://youtu.be/nPD7iIGRZ5Q



## Github

You can view all of the code related to this project on our Github: https://github.com/BrianBock/ENPM661-Project3-Phase-4

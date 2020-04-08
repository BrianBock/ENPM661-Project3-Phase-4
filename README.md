# ENPM661 Project 3 Phase 4 - Simulation

## Introduction

The goal of this project is to find the optimal path through a Cartesian maze with obstacles for a rigid robot using the A* algorithm. The robot for this project is the Turtlebot, a two wheeled differential drive robot. It has 8 possible movements, defined by a combination of 3 speeds for the left and right wheels (user defined Fast, Slow, and 0). The default maze is 10200x10200 with 8 obstacles - 4 circles, 3 squares, and a hollow rectangle at the border.

![maze](https://github.com/BrianBock/ENPM661-Project3-Phase3-4/blob/master/Images/V-Rep_maze.png)

The user specifies a start point and goal point in the maze and the program finds the optimal path to the goal.

## Dependencies 

    cv2
    numpy
    matplotlib
    matplotlib.backends.backend_agg
    matplotlib.collections
    matplotlib.patches
    matplotlib.pyplot
    datetime
    bisect
    math
    os


## Instructions for Running the Program - Phase 3

To run the program, clone this repository to a directory you have write access to. Open a new terminal window and navigate to the Phase 3 directory. Type `python main.py`, if you have additional older versions of python installed you may need to run `python3` instead. 

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


## Output

The program has several boolean toggles at the top of the of the `main.py` file. If `write_to_video` is set to `True`, the program will output a video of the solution. To do this, the program generates individual frames, saved to the same directory as the code (the second reason you must have write access).

If `show_visualization` is set to `True`, the program will show the visualization as it is being created. 

**Note that `show_visualization` and `write_to_video` are mutually exclusive. You can export the video or you can watch the visualization as it runs, but you cannot do both.** You can run `show_solve` with either visualization or video. 

If `show_solve` is set to `False`, the program will only export an animation of the final path. If you would like to see the full visualization including all searched nodes, toggle `show_solve` to `True`. To speed this up, we only save every `k` frames, a number which can be changed by editing `solve_frame_interval` in the top of `main.py`. Lower intervals will be much slower to export, but have smoother video. If `show_solve` is set to `True`, the visualization first shows all of the searched nodes, rendered as semi-transparent purple squares. The height and width of these squares is determined by our position threshold (`self.pos_thresh` in `robot.py`) by which we discretize our space. Each node can be visited N times, where N=360 deg/angular_thresh. After a searched node is within the goal, the program uses backtracking to find the optimal course which is plotted with orange lines. 

![visualization](https://github.com/BrianBock/ENPM661-Project3-Phase3-4/blob/master/Images/visualization_path-only.gif)
![Full visualization](https://github.com/BrianBock/ENPM661-Project3-Phase3-4/blob/master/Images/full_viz.gif)

## Videos

Full Visualization: Start(500,500,90), Goal(9500,9500) - https://youtu.be/YgzpRYx1qZM

Start(1100,1000,90), Goal(7000, 6120) - https://youtu.be/C3S3WZDgzS4

Start(1100,1000,90), Goal(8160, 4080) - https://youtu.be/mdABzRMgJLM

Start(1100,1000,90), Goal(9000,9000) - https://youtu.be/rJ3gQGppOLo

Start(1100,1000,90), Goal(5000,8160) - https://youtu.be/Q-o_nECJxok



## Github

You can view all of the code related to this project on our Github: https://github.com/BrianBock/ENPM661-Project3-Phase3-4

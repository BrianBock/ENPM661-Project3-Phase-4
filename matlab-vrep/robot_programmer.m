%% Project Setup
clc
clear all
global vrep;
global clientID;
global wheel_separation_width;
global wheel_radius;
global wheel_separatation_length;
global Turtle_Right_Wheel;
global Turtle_Left_Wheel;
global Fast;
global Slow;
global moveTime;

wheel_separation_width=.5/2;%m
wheel_radius=.035; %meters
wheel_separatation_length=.235; %m

Fast=15;
Slow=10;
moveTime=1;


%% Connect to VRep

vrep=remApi('remoteApi'); % using the prototype file (remoteApiProto.m)
vrep.simxFinish(-1); % just in case, close all opened connections

clientID=vrep.simxStart('127.0.0.1',19999,true,true,5000,5);


if (clientID<=-1) % If not true, we've connected
    disp('Cannot connect to VRep. Make sure the Vrep simulation is already running');
    return;
end

if(clientID>-1)
disp('Connected to vrep. Ready to go!');
end

%% Get Object Handles for all Parts

[~, Turtle_Right_Wheel]=vrep.simxGetObjectHandle(clientID, 'wheel_right_joint', vrep.simx_opmode_blocking);
[~, Turtle_Left_Wheel]=vrep.simxGetObjectHandle(clientID, 'wheel_left_joint', vrep.simx_opmode_blocking); 


%% Drive the Robot
%pause(10);
move(Fast,Fast)
move(Fast,Slow)
move(Fast,0)


pause(1)
move(Slow,Fast)
move(Slow,Slow)
move(Slow,0)







vrep.simxFinish(-1); % Close the connection

vrep.delete(); % Call the vrep destructor




%% Functions
function mover=move(left_speed, right_speed)% Drive Forward (direction =1), Reverse (direction=-1)
global clientID;
global vrep;
global Turtle_Right_Wheel;
global Turtle_Left_Wheel;
global moveTime;


%spin wheels
[~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,right_speed,vrep.simx_opmode_blocking);
[~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,left_speed,vrep.simx_opmode_blocking);
pause(moveTime)
%stop wheels
[~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,0,vrep.simx_opmode_blocking);
[~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,0,vrep.simx_opmode_blocking);
pause(.5);




end







function driver=drive(distance, speed)% Drive Forward (direction =1), Reverse (direction=-1)
global clientID;
global vrep;
global Turtle_Right_Wheel;
global Turtle_Left_Wheel;
global Fast;
global Slow;


if(speed>0)
    disp("Driving Foward!");
elseif(speed<0)
    disp("Beep beep beep - driving backwards!");
end
        wheel_velocity=speed;
        duration=abs(distance/(.3*speed));
        %spin wheels
        [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,wheel_velocity,vrep.simx_opmode_blocking);
        [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,wheel_velocity,vrep.simx_opmode_blocking);
        pause(duration)
        %stop wheels
        [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,0,vrep.simx_opmode_blocking);
        [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,0,vrep.simx_opmode_blocking);
        pause(.5);
end


% function driver=drive(wheel_velocity,duration,direction)% Drive
% Forward (direction =1), Reverse (direction=-1)
%Original drive function, uses wheel_speed and time
% global clientID;
% global vrep;
% global KMR_Front_Right_Wheel;
% global KMR_Front_Left_Wheel;
% global KMR_Rear_Right_Wheel;
% global KMR_Rear_Left_Wheel;
% 
% if(direction==1)
%     disp("Driving Foward!");
% elseif(direction==-1)
%     disp("Beep beep beep - driving backwards!");
% end
%         wheel_velocity=wheel_velocity*direction;
%         %spin wheels
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Front_Left_Wheel,wheel_velocity,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Front_Right_Wheel,-wheel_velocity,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Rear_Right_Wheel,-wheel_velocity,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Rear_Left_Wheel,wheel_velocity,vrep.simx_opmode_blocking);
%         pause(duration)
%         %stop wheels
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Front_Left_Wheel,0,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Front_Right_Wheel,0,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Rear_Left_Wheel,0,vrep.simx_opmode_blocking);
%         [~]=vrep.simxSetJointTargetVelocity(clientID,KMR_Rear_Right_Wheel,0,vrep.simx_opmode_blocking);
% end


function pivot=rotate(angle) % Rotate about central axis (deg)
    global clientID;
    global vrep;
    global Turtle_Right_Wheel;
    global Turtle_Left_Wheel;
    global KMR_Rear_Right_Wheel;
    global KMR_Rear_Left_Wheel;
    global wheel_radius;
    global wheel_separation_width
    global wheel_separatation_length
    angle=deg2rad(angle);
    
    disp("Turning!");
    % https://robohub.org/drive-kinematics-skid-steer-and-mecanum-ros-twist-included/
    v_wheel_left = 5
    v_wheel_right = -5

    %spin wheels
    [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,v_wheel_right,vrep.simx_opmode_blocking);
    [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel, v_wheel_left,vrep.simx_opmode_blocking);
    pause(1)
    %stop wheels
    [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Right_Wheel,0,vrep.simx_opmode_blocking);
    [~]=vrep.simxSetJointTargetVelocity(clientID,Turtle_Left_Wheel,0,vrep.simx_opmode_blocking);
    pause(.5);
end







% if (vrep.simxGetObjectInt32Parameter(shape,sim.shapeintparam_static)==0) and (sim.getObjectInt32Parameter(shape,sim.shapeintparam_respondable)~=0) and (sim.checkProximitySensor(objectSensor,shape)==1) then
% %Ok, we found a non-static respondable shape that was detected
% attachedShape=shape
% %Do the connection:
% end

% ?-- You have basically 2 alternatives to grasp an object:
%     --
%     -- 1. You try to grasp it in a realistic way. This is quite delicate and sometimes requires
%     --    to carefully adjust several parameters (e.g. motor forces/torques/velocities, friction
%     --    coefficients, object masses and inertias)
%     --
%     -- 2. You fake the grasping by attaching the object to the gripper via a connector. This is
%     --    much easier and offers very stable results.
%     --
%     -- Alternative 2 is explained hereafter:
%     --
%     --
%     -- a) In the initialization phase, retrieve some handles:
%     -- 
%     -- connector=sim.getObjectHandle('RG2_attachPoint')
%     -- objectSensor=sim.getObjectHandle('RG2_attachProxSensor')
%     
%     -- b) Before closing the gripper, check which dynamically non-static and respondable object is
%     --    in-between the fingers. Then attach the object to the gripper:
%     --
%     -- index=0
%     -- while true do
%     --     shape=sim.getObjects(index,sim.object_shape_type)
%     --     if (shape==-1) then
%     --         break
%     --     end
%     --     if (sim.getObjectInt32Parameter(shape,sim.shapeintparam_static)==0) and (sim.getObjectInt32Parameter(shape,sim.shapeintparam_respondable)~=0) and (sim.checkProximitySensor(objectSensor,shape)==1) then
%     --         -- Ok, we found a non-static respondable shape that was detected
%     --         attachedShape=shape
%     --         -- Do the connection:
%     --         sim.setObjectParent(attachedShape,connector,true)
%     --         break
%     --     end
%     --     index=index+1
%     -- end
%     
%     -- c) And just before opening the gripper again, detach the previously attached shape:
%     --
%     -- sim.setObjectParent(attachedShape,-1,true)

% end



function move(t_rightWheel,t_leftWheel,left_speed, right_speed,moveTime)

	sim.setJointTargetVelocity(t_rightWheel,right_speed)
    sim.setJointTargetVelocity(t_leftWheel,left_speed)

    sim.wait(moveTime)

	sim.setJointTargetVelocity(t_rightWheel,0)
    sim.setJointTargetVelocity(t_leftWheel,0)

    sim.wait(.1)

end



-- function getHandles()
--     t_rightWheel  = sim.getObjectHandle('wheel_right_joint')
--     t_leftWheel   = sim.getObjectHandle('wheel_left_joint')

--     return t_rightWheel, t_leftWheel
-- end


function sysCall_threadmain()
	Fast=80
	Slow=20
	moveTime=5
    t_rightWheel = sim.getObjectHandle('wheel_right_joint')
    t_leftWheel  = sim.getObjectHandle('wheel_left_joint')

    move(Fast, Slow, moveTime)
    
end

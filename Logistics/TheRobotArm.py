from pyjop import *

#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()
env.reset()

#Get Robot arm
arm = RobotArm.first()

    #[x,y,z]
#x (forward);
#y (right) (so actually 1 meter to the left);
#z (up);

arm.set_grabber_location([1.5,0,0]) # Move arm forward
sleep(2) # Sleep to pick up

arm.pickup() # Pick up barrel
arm.set_grabber_location([-3,1,3]) # Move to dumpster
sleep(2) # sleep to move item

arm.release() # Let go and hope for the best

#cleanup close code
SimEnv.disconnect()

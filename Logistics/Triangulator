#import the joy of programming python module pyjop
from pyjop import *
#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()
env.reset()

    #object variables 
platform = MovablePlatform.find("platform")
robotArm = RobotArm.find("arm")
pointB = RangeFinder.find("B").get_distance()
pointC = RangeFinder.find("C").get_distance()

    #Logic
platform.set_target_location(3.5+pointB,5.3+pointC,0) #Move
sleep(5)
robotArm.set_grabber_location([1.8,0,0.5])
sleep(3)
robotArm.pickup()
sleep(1)
robotArm.set_grabber_location([-3,0,3])
sleep(3)#for some reason will keep moving with out this pause
platform.set_target_location([-1,0,0])
sleep(3)
robotArm.release()
    
#cleanup close code
SimEnv.disconnect()

from pyjop import *

#connect to the current SimEnv
SimEnv.connect()

#create references to entities in the SimEnv
env = SimEnvManager.first()
env.reset()


#----------Controllable Items------------# 

#Conveyor belts
conv0 = ConveyorBelt.find("belt0").set_target_speed(5) #Run by default
conv1 = ConveyorBelt.find("belt1") #Left or right
conv2 = ConveyorBelt.find("belt2").set_target_speed(5)
conv3 = ConveyorBelt.find("belt3").set_target_speed(4)
conv4 = ConveyorBelt.find("belt4") #Left or right

#Scanners & tags 
scanner0 = RangeFinder.find("scan0")
scanner1 = RangeFinder.find("scan1")

while SimEnv.run_main():
    tag1 = scanner0.get_rfid_tag()
    tag2 = scanner1.get_rfid_tag()


    #-----------LOGIC----------------#
    if (tag1 == "Barrel"):
        print("Barrel Detected")
        conv1.set_target_speed(-5)
    elif (tag1 == "Box" or tag1 == "Cone"):
        print("Box or Cone Detected")
        conv1.set_target_speed(5)  

    
    if (tag2 == "Box"):
        print("Box detected")
        conv4.set_target_speed(-5)
    elif (tag2 == "Cone"):
        print("Cone detected")
        conv4.set_target_speed(5)

    if(ConveyorBelt.find("belt0").get_is_transporting() == False): 
        print("Spawning Item...")
        sleep(5)
        ObjectSpawner.find("spawner").spawn()
    #--------------------------------#

#cleanup close code
SimEnv.disconnect()
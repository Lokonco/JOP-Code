from pyjop import *
SimEnv.connect()

sensor = ProximitySensor.first()
alarm = AlarmSiren.first()

#Main Loop
while SimEnv.run_main():
    for dat in sensor.get_proximity_data():
        if dat.entity_type == "HumanoidRobot" and dat.distance < 2.3:
            alarm.set_alarm_enabled(True)
            break

#cleanup close code
SimEnv.disconnect()

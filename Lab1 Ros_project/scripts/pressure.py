#!/usr/bin/env python3

import rospy
import random
from ros_project.msg import sensor_readings



def publish_pressure():

    rospy.init_node('pressure_node',anonymous=True)
    pub_pressure = rospy.Publisher('pressure_data',sensor_readings,queue_size=10)

    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        
        rate.sleep()
        # Actual humidity range + Out of range values for Validation
        sensor_reading = random.uniform(0.8, 1.3) #0.95 atm <= p <= 1.2 atm

        # random.random()  Random number between 0.0 and 1.0
        PressureSensor_state = random.random() < 0.91 # 91% probability of choosing True
        
        sensor_state_msg = sensor_readings()
        sensor_state_msg.sensor_name = 'Pressure'
        sensor_state_msg.state = PressureSensor_state
        
        if PressureSensor_state == False:
            sensor_state_msg.value = 0.0
        else:
            sensor_state_msg.value = sensor_reading



        rospy.loginfo(" . SensorState : %s , Pressure: %.2f, ", "Working" if PressureSensor_state else "Not Working ", sensor_reading)
        if PressureSensor_state == False:
            rospy.logwarn("Pressure Sensor is not working properly, Please check the sensor") 

        pub_pressure.publish(sensor_state_msg)

        rate.sleep()

      
if __name__ == '__main__':
   
    publish_pressure()
    
    
    

    
#Validation for remote station node 

        # if .7 <= sensor_reading <= .95 : 
        #     temp_node_state = 'true'
        # else:
        #     temp_node_state = 'false'
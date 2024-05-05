#!/usr/bin/env python3

import rospy
import random

from ros_project.msg import sensor_readings

def publish_temp():

    rospy.init_node('temp_node',anonymous=True)

    pub_temp= rospy.Publisher('temperature_data',sensor_readings,queue_size=10)

    
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        rate.sleep()
        # Actual temperature range + Out of range values for Validation
        sensor_reading = random.randint(1,110) #10 <= t <= 100
        
        
        # random.random()  Random number between 0.0 and 1.0
        temperature_Sensor_state = random.random() < 0.91 # 91% probability of choosing True
        
        sensor_state_msg = sensor_readings()
        sensor_state_msg.sensor_name = 'temperature'
        sensor_state_msg.state = temperature_Sensor_state
        
        if temperature_Sensor_state == False:
            sensor_state_msg.value = 0.0
        else:
            sensor_state_msg.value = sensor_reading

        
        rospy.loginfo(". SensorState : %s , temperature: %.2f, ", "Working" if temperature_Sensor_state else "Not Working ", sensor_state_msg.value)
        if temperature_Sensor_state == False:
            rospy.logwarn("temperature Sensor is not working properly, Please check the sensor") 

        
        pub_temp.publish(sensor_state_msg)


        rate.sleep()


 
if __name__ == '__main__':
   
    publish_temp()
    
    
    
#Validation for remote station node 

# if 10 <= sensor_reading <= 100 : 
#     temp_node_state = 'True'
# else:
#     temp_node_state = 'False'